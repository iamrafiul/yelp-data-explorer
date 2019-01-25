# Exploring Yelp open dataset using spark and cassandra

The repo. does three jobs: 

*  Parse YELP open dataset and save it in (any)tabular format using SMACK stack.
*  Write queries against the data to verify that everything works.
*  Dockerize the program.

We shall setup and go through them one by one.

## Setup and Run

This section describes how to setup the project and run it step by step.

### Setup

Clone the project.

To setup the environment for running the project, do the following:
* Download and install Docker from [here](https://docs.docker.com/docker-for-mac/install/).
* Download and install Docker compose from [here](https://docs.docker.com/compose/). If you are using the docker app of Mac, you need not to install it
separately, docker-compose comes built in with this app.
* Go to the project directory in your machine and [download yelp open dataset](https://www.yelp.com/dataset/download).
It's more than 3 GB so will take some time.
* Make sure the `.tar` file is in your project directory.

We can run the project without containerizing it. It is competitively easy if you install cassandra and run it in your local machine, create 
a virtual environment, install the dependencies and run the python code. If you want to do that, I have described how to do so in the `Run` section.

We containerize our code so that it becomes non-OS/Machine dependent which is an industry standard now. Once you containerize your project, 
anyone can run the project by creating the docker containers, no matter which OS/Machine they are using. Containerization frameworks such as Docker 
takes care of it, that's the beauty of containerization.
 

In the next step, we shall create docker containers to run the project.

### Run

#### Without Docker

I am assuming you have python 3+ and have alredy downloaded the yelp dataset `.tar` file and it's in your project directory.

Now do the following:
* Install java in [Linux](http://tipsonubuntu.com/2016/07/31/install-oracle-java-8-9-ubuntu-16-04-linux-mint-18/) or [Mac](https://www.cs.dartmouth.edu/~scot/cs10/mac_install/mac_install.html).
* Set Java 8 as your main java version using JAVA_HOME variable. For me, java home was the following in my mac
```
JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home
```
* Set SPARK_HOME variable. For me, it was like this:
```
SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.0
```
* Download and install cassandra in [Linux](https://www.vultr.com/docs/how-to-install-apache-cassandra-3-11-x-on-ubuntu-16-04-lts) or [Mac](https://medium.com/@areeves9/cassandras-gossip-on-os-x-single-node-installation-of-apache-cassandra-on-mac-634e6729fad6)
* Create a virtual environment in the project directory and activate it
```
virtualenv -p python3 venv
source venv/bin/activate
```
* Install the packages from requirements.txt using pip
```
pip install -r requirements.txt
```
* Run cassandra from shell
```
cassandra -f
```
* Run the following command:
```
$SPARK_HOME/bin/spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 yelp_data_extractor.py -f yelp_dataset.tar
```

If everything goes well, you will see that spark has started the spark-submit job, untar'ing the data into json files and writing them into cassandra tables. It will take a while, be patient. 

#### With Docker

So we want to containerize our project before running it. The idea is to run two docker containers, one for spark(along with our code) & one for 
cassandra. We shall run our code from the spark container and save the yelp data in the cassandra database which is in another container.

Before creating the containers from the images, you need to consider/understand few things. In a production environment, there should be several docker
containers for different services and they communicate among them. To maintain and run this `multi-container applications` easily, you can create a 
configuration file in docker which will contain the details of all the docker containers and define the network though which they shall communicate 
with each other.

This file is called `docker-compose.yml` and you can run all the containers you have mentioned in that file using the following command:
```
docker-compose up
```
This will build, (re)create, start, and attach to containers for a service.


> ##### A bit of background before running
> 
> Before running the docker compose, let me tell you something. 
> 
> If we run multiple Docker containers and want to make communication between them, we need to create network so that all the containers which will 
> communicate with each other know which network to go for communicating with a specific container. Network in docker is a very important concept as 
> we run multi-container system in real time scenario(i. e. production environment). If you use Kubernetes(K8) for docker orchestration, they have 
> their own `kubernetes model` to communicate between pods.
> 
> As we're not using K8 here, we shall go with the regular docker networking model. 

Run
```
docker-compose up
```
Docker will create the containers and will run the `spark-submit` job. If everything goes well, you will have all the data in cassandra under the keyspace
`yelp_data`.

It will take some time becasue of the extraction of `.tar` file. Also, the amount of data is more than 8 GB and we are running only one cluster of 
cassandra which is not optimal.


I have done these steps in a macbook pro. You can use any OS and setup these things accordingly.