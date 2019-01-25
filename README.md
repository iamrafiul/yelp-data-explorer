# Exploring Yelp open dataset using spark and cassandra

The repo. does three jobs: 

*  Parse [YELP open dataset](https://www.yelp.com/dataset/download) and save it in database in tabular format.
*  Write queries against the data to verify that everything works.
*  Dockerize the project.

## Step 1: Create Database schema
Schema creation is done by `cql_schema_creator.py`. It connects to the cassandra database 
using the cassandra host provided in `spark-submit` job and creates the keyspace and tables
from the given CQL.

## Step 2: Parsing YELP open dataset and Insert data into cassandra table
This is done by the `yelp_data_extractor.py`. It takes a file as argument with `-f` flag and
extracts the tar file in a sub-directory named `data/`.

Data insertion is done by following steps:

1. List all the json files from `data/` directory 
2. Read them one by one and extract the table name from the JSON file name.
3. Insert data into that table in cassandra using Spark.

## Step 4: Dockerize the project and run.
 
We shall go through this step one by one.

### Setup and Run

This section describes how to setup the project and run it step by step.

#### Setup

Clone the project.

Setup the environment to run the project:
* Download and install Docker from [here](https://docs.docker.com/docker-for-mac/install/).
* Download and install Docker compose from [here](https://docs.docker.com/compose/). If you are using the docker app of Mac, you need not to install it
separately, docker-compose comes built in with this app.
* [Download yelp open dataset](https://www.yelp.com/dataset/download). It's more than 3 GB so will take some time.
* Copy the `.tar` file into the project directory of your machine.

You can run the project without containerizing it. It is competitively easy if you install cassandra and run it in your local machine, create 
a virtual environment, install the dependencies and run the `spark-submit` job.

Instead of doing so, we shall containerize the project so that it becomes non-OS/Machine dependent which is an industry standard now. Once you containerize your project, 
anyone can build and run the project, no matter which OS/Machine they are using. Containerization frameworks such as Docker 
takes care of it, that's the beauty of containerization.

In the next step, we shall use docker to build and run our project.

#### Run

So we want to containerize our project before running it. The idea is to run two docker containers, one for spark(along with our code) and one for 
cassandra. We shall run our code from the spark container and save the yelp data in the cassandra database which will be in another container.

As this will be a `multi-container applications`, instead of doing everything by ourself, 
we shall create a configuration file in docker which will take care of building and running 
the container, make them available in network(s) and hence, will leverage our effort and time.

The file we shall write these configuration is called `docker-compose.yml` and we shall run 
that file using `docker-compose` which we have already installed.

> ##### A bit of `networking` in docker
> 
> If we run multiple Docker containers and want to make communication between them, we need 
> to create network(s) so that the containers know which network to connect for which 
> container. Networking in docker is a very important concept as we mostly run multi-container 
> system in real time scenario(i. e. production environment). 
> 
> As we're using `docker-compose`, it will take care of the networking for us as well.

First `build` the project with `docker-compose` using  
```
sudo DATA_FILE_PATH=./yelp_dataset.tar docker-compose build 
```
And then run it using the `up` command

```
sudo DATA_FILE_PATH=./yelp_dataset.tar docker-compose up 
```

> `DATA_FILE_PATH` is the volume(in our case the yelp tar file) we're giving to docker as a file which will be 
processed using a `spark-submit` job.

This will build, (re)create, start, and attach to containers for a service. 
 
If everything goes well, docker compose will create the containers, attach them, run the `spark-submit` 
job to untar the file, save data into cassandra and query the table to check if the data is ok.

> It will take some time because of the extraction of big `.tar` file and the amount of data
 will be more than 8 GB which we are processing in a single cassandra cluster of cassandra 
 which is not optimal.

You will see the query results in console.