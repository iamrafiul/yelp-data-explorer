#!/usr/bin/env bash
#/spark/bin/spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 yelp_data_extractor.py -f $1

/spark/bin/spark-submit --conf spark.cassandra.connection.host=cassy --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 /app/yelp_data_extractor.py -f $1

#/spark/bin/spark-submit --conf spark.cassandra.connection.host=cassy --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 /app/yelp_data_extractor.py -f /app/yelp_dataset.tar