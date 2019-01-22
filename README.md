# Exploring Yelp open dataset using spark and cassandra

The repo. does three jobs: 

*  Parse YELP open dataset and save it in (any)tabular format using SMACK stack.
*  Write queries against the data to verify that everything works.
*  Dockerize the program.

We shall setup and go through them one by one.

## Part 1

To run this task, make sure:
* You have java 8 installed and $JAVA_HOME is set to java 8
* You have spark installed and $SPARK_HOME is set to the path. [You can install it from this link for mac](https://medium.freecodecamp.org/installing-scala-and-apache-spark-on-mac-os-837ae57d283f).
* You have Cassandra installed. [You can install it from this link for mac](https://gist.github.com/hkhamm/a9a2b45dd749e5d3b3ae).

I have done these steps in a macbook pro. You can use any OS and setup these things accordingly.