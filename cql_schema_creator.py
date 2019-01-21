from cassandra.cluster import Cluster


class CassandraSchemaGenerator:
    def __init__(self, keyspace):
        self.keyspace = keyspace
        self.cluster = Cluster(['127.0.0.1'], port=9042)
        self.cluster_conn = self.cluster.connect()

    def create_schema(self):
        self.cluster_conn.execute ("DROP keyspace IF EXISTS " + self.keyspace + ";")
        self.cluster_conn.execute (
            "CREATE keyspace IF NOT EXISTS " + self.keyspace + " WITH REPLICATION = {'class' : 'SimpleStrategy','replication_factor' : 1 };")
        print ("Created keyspace: {}".format (self.keyspace))

        table = "business"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                    business_id text PRIMARY KEY, \
                    name text, \
                    address text, \
                    city text,  \
                    state text,  \
                    postal_code text,  \
                    latitude text,  \
                    longitude text,  \
                    stars text,  \
                    review_count text,  \
                    is_open text,  \
                    attributes text,  \
                    categories text,  \
                    hours text);")

        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        table = "review"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       review_id text PRIMARY KEY, \
                       user_id text, \
                       business_id text,  \
                       stars text, \
                       useful text,  \
                       funny text,  \
                       cool text,  \
                       text text,  \
                       date text);")
        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        table = "user"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       user_id text PRIMARY KEY, \
                       name text, \
                       review_count text,  \
                       yelping_since text, \
                       friends text,  \
                       useful text,  \
                       funny text,  \
                       cool text,  \
                       fans text,  \
                       elite text,  \
                       average_stars text,  \
                       compliment_hot text,  \
                       compliment_more text,  \
                       compliment_profile text,  \
                       compliment_cute text,  \
                       compliment_list text,  \
                       compliment_note text,  \
                       compliment_plain text,  \
                       compliment_cool text,  \
                       compliment_funny text,  \
                       compliment_writer text,  \
                       compliment_photos text);")
        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        table = "photo"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                            photo_id text PRIMARY KEY, \
                            business_id text, \
                            caption text, \
                            label text);")
        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        table = "checkin"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       business_id text, \
                       date text,  \
                       PRIMARY KEY (business_id));")

        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        table = "tip"

        self.cluster_conn.execute ("DROP TABLE IF EXISTS " + self.keyspace + "." + table + ";")
        self.cluster_conn.execute ("CREATE TABLE IF NOT EXISTS " + self.keyspace + "." + table + " ( \
                       user_id text,  \
                       business_id text, \
                       text text, \
                       date text, \
                       compliment_count int,  \
                       PRIMARY KEY (business_id,user_id));")
        print ("Created Table \'{}\' within keyspace \'{}\'".format (table, self.keyspace))

        return