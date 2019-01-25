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

You can run the project without containerizing it. It is competitively easy if you install cassandra and run it in your local machine, create 
a virtual environment, install the dependencies and run the `spark-submit` job.

We containerize our code so that it becomes non-OS/Machine dependent which is an industry standard now. Once you containerize your project, 
anyone can run the project by creating the docker containers, no matter which OS/Machine they are using. Containerization frameworks such as Docker 
takes care of it, that's the beauty of containerization.
 

In the next step, we shall use docker to build and run our project.

### Run

So we want to containerize our project before running it. The idea is to run two docker containers, one for spark(along with our code) & one for 
cassandra. We shall run our code from the spark container and save the yelp data in the cassandra database which is in another container.

Before creating the containers from the images, you need to consider/understand few things. In a production environment, there should be several docker
containers for different services and they communicate among them. To maintain and run this `multi-container applications` easily, you can create a 
configuration file in docker which will contain the details of all the docker containers and define the network though which they shall communicate 
with each other.

This file is called `docker-compose.yml` and you can run all the containers you have mentioned in that file using this.

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
This will build, (re)create, start, and attach to containers for a service. Docker will create the containers and will run the `spark-submit` job. If everything goes well, you will have all the data in cassandra under the keyspace
`yelp_data`.

It will take some time becasue of the extraction of `.tar` file. Also, the amount of data is more than 8 GB and we are running a single cluster of 
cassandra which is not optimal.


I have done these steps in a macbook pro. You can use any OS and setup these things accordingly.