# -*- coding: utf-8 -*-
"""
    Cassandra data explorer.

    Runs query on cassandra cluster to check if there is data in tables.
"""

from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as f
from cassandra.cluster import Cluster


class CassandraDataExplorer:
    # Constructor
    def __init__(self):
        self.cluster = Cluster(['cassandra'])
        self.cluster_conn = self.cluster.connect()

        self.sc = SparkContext("local", "Cassandra Data Explorer")
        self.sqlContext = SQLContext(self.sc)

    def load_and_get_table_df(self, table_name, keyspace):
        """
            Fetch data from cassandra and load in pyspark Dataframe.
        :param table_name: Name of the table.
        :param keyspace: Name of the keyspace in database.
        :return:
            dataframe (obj): Pyspark dataframe.
        """
        table_df = self.sqlContext.read\
            .format("org.apache.spark.sql.cassandra")\
            .options(table=table_name, keyspace=keyspace)\
            .load()
        return table_df

    def explore_data(self):
        """
            Run queries on cassandra table dataframe and show
            first 20 results. Doesn't save data anywhere.
        :return:
        """
        business_df = self.load_and_get_table_df('business', 'yelp_data')
        user_df = self.load_and_get_table_df('user', 'yelp_data')
        review_df = self.load_and_get_table_df('review', 'yelp_data')
        checkin_df = self.load_and_get_table_df('checkin', 'yelp_data')
        tip_df = self.load_and_get_table_df('tip', 'yelp_data')
        photo_df = self.load_and_get_table_df('photo', 'yelp_data')

        # Business with rating above 4.5 and review count more than 1000
        business_df = business_df.\
            select("name", "city", "review_count", "stars")\
            .where(
                (f.col("stars").between(2, 2.5)) &
                (f.col("review_count") > 1000)
            )\
            .orderBy("city")
        business_df.show()

        # Users with more than 100 review count and average star
        # rating above 4.5
        user_df = user_df.select("user_id", "name", "review_count")\
            .where(
                (f.col("review_count") > 100) &
                (f.col("average_stars") > 4.5)
            )
        user_df.show()

        # Review with rating more than 4.5 and was useful to
        # at least 10 people.
        review_df = review_df.select("review_id", "text")\
            .where(
                (f.col("stars") > 4.5) &
                (f.col("useful") >= 10)
            )
        review_df.show()

        # Tips given between 2018-01-01 to 2018-02-28 & having
        # at least 2 compliments
        tip_df = tip_df.select("text", "date", "compliment_count")\
            .where(
                (f.col("date").between('2018-01-01', '2018-02-28')) &
                (f.col("compliment_count") >= 2)
            )
        tip_df.show()

        # Photo id with label 'Drink'
        photo_df = photo_df.select("photo_id", "label")\
            .where(f.col("label").like("%drink%"))
        photo_df.show()

        # Businesses which have at least one checkin at 2017-01-01
        checkin_df = checkin_df.select("business_id") \
            .where(f.col("date").like("%2017-01-01%"))
        checkin_df.show()


if __name__ == '__main__':
    data_explorer = CassandraDataExplorer()
    data_explorer.explore_data()
