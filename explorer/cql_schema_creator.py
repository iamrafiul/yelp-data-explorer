# -*- coding: utf-8 -*-
"""
    Schema generator for cassandra database.

    Creates database keyspace and tables based on SQL.
"""

from cassandra.cluster import Cluster


class CassandraSchemaGenerator:
    # Constructor
    def __init__(self, keyspace):
        self.keyspace = keyspace
        self.cluster = Cluster(['cassandra'])
        self.cluster_conn = self.cluster.connect()

    def create_schema(self):
        """
            Create cassandra database keyspace and tables based on the
            SQLs provided.
        :return:
        """
        self.cluster_conn.execute(
            "DROP keyspace IF EXISTS " + self.keyspace + ";")
        self.cluster_conn.execute(
            "CREATE keyspace IF NOT EXISTS " + self.keyspace +
            " WITH REPLICATION = {'class' : 'SimpleStrategy',"
            "'replication_factor' : 1 };")
        print("Created keyspace: {}".format(self.keyspace))

        table = "business"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                    business_id text PRIMARY KEY, \
                    name text, \
                    address text, \
                    city text,  \
                    state text,  \
                    postal_code text,  \
                    latitude float,  \
                    longitude float,  \
                    stars float,  \
                    review_count int,  \
                    is_open int,  \
                    attributes text,  \
                    categories text,  \
                    hours text);")

        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        table = "review"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       review_id text PRIMARY KEY, \
                       user_id text, \
                       business_id text,  \
                       stars int, \
                       useful int,  \
                       funny int,  \
                       cool int,  \
                       text text,  \
                       date text);")
        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        table = "user"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       user_id text PRIMARY KEY, \
                       name text, \
                       review_count int,  \
                       yelping_since text, \
                       friends text,  \
                       useful int,  \
                       funny int,  \
                       cool int,  \
                       fans int,  \
                       elite text,  \
                       average_stars float,  \
                       compliment_hot int,  \
                       compliment_more int,  \
                       compliment_profile int,  \
                       compliment_cute int,  \
                       compliment_list int,  \
                       compliment_note int,  \
                       compliment_plain int,  \
                       compliment_cool int,  \
                       compliment_funny int,  \
                       compliment_writer int,  \
                       compliment_photos int);")
        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        table = "photo"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                            photo_id text PRIMARY KEY, \
                            business_id text, \
                            caption text, \
                            label text);")
        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        table = "checkin"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       business_id text, \
                       date text,  \
                       PRIMARY KEY (business_id));")

        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        table = "tip"

        self.cluster_conn.execute("DROP TABLE IF EXISTS " + self.keyspace +
                                  "." + table + ";")
        self.cluster_conn.execute(
            "CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       user_id text,  \
                       business_id text, \
                       text text, \
                       date text, \
                       compliment_count int,  \
                       PRIMARY KEY (business_id,user_id));")
        print("Created Table \'{}\' within keyspace \'{}\'"
              .format(table, self.keyspace))

        return
