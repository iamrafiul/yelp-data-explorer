import os
import sys
import argparse
import tarfile
import glob

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python'

from cql_schema_creator import CassandraSchemaGenerator
from pyspark.sql import SparkSession, SQLContext


class YelpDataProcessor:
    def __init__(self, keyspace, data_dir):
        self.keyspace = keyspace
        self.spark = SparkSession.builder \
            .master("local") \
            .appName("Newyorker Yelp Data Ingestor") \
            .config("spark.debug.maxToStringFields", 500) \
            .getOrCreate()

        # .set("spark.cassandra.connection.host", "0.0.0.0") \

        self.sqlContext = SQLContext(self.spark)
        self.data_dir = data_dir

    def list_json_files(self):
        try:
            files = glob.glob(self.data_dir + '/*.json')
            files = map(lambda x: x.split('/')[-1], files)
            return files
        except OSError as e:
            print(e)
        return

    def process_data(self):
        try:
            files = self.list_json_files()
            for file in files:
                table_name = file.split('.')[0]
                print('Table name: ' + table_name)
                df = self.sqlContext.read.json(self.data_dir + '/' + file)
                df.write.format("org.apache.spark.sql.cassandra")\
                    .mode("ignore")\
                    .options(table=table_name, keyspace=self.keyspace)\
                    .save()
                print('Wrote data in table {} for keyspace {}'.format(table_name, self.keyspace))
        except Exception as e:
            print(e)

    def extract_tar_file(self, filename):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        output_dir = dir_path + '/data'
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        if filename.endswith('.tar'):
            tar = tarfile.open(filename)
            print('Started extracting Yelp data set.')
            tar.extractall(path=output_dir)
            tar.close()
            print('Yelp data extracted in directory: {}'.format(output_dir))


if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        dest="tar_file",
                        help="Provide a valid path for the yelp tar file",
                        metavar="FILE")
    args = parser.parse_args()

    if args.tar_file:
        keyspace = "yelp_data"

        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_dir = dir_path + '/data'

        yelp_processor = YelpDataProcessor(keyspace=keyspace, data_dir=data_dir)

        # print("Start extracting tar file.")
        # yelp_processor.extract_tar_file(args.tar_file)
        # print('Successfully extracted tar file in directory \'{}\''.format(data_dir))

        print("Start building Cassandra schemas.")
        schema_builder = CassandraSchemaGenerator(keyspace)
        schema_builder.create_schema()
        print("Successfully build Cassandra schemas.")

        print("Start inserting data from JSON to Cassandra tables.")
        yelp_processor.process_data()
        print("Successfully inserted data into Cassandra tables.")
