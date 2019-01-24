$SPARK_HOME/bin/spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 yelp_data_extractor.py -f $1
