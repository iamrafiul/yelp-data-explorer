#FROM sequenceiq/hadoop-docker:2.6.0
#MAINTAINER SequenceIQ
#
##support for Hadoop 2.6.0
#RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.6.1-bin-hadoop2.6.tgz | tar -xz -C /usr/local/
#RUN cd /usr/local && ln -s spark-1.6.1-bin-hadoop2.6 spark
#ENV SPARK_HOME /usr/local/spark
#RUN mkdir $SPARK_HOME/yarn-remote-client
#ADD yarn-remote-client $SPARK_HOME/yarn-remote-client
#
#RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.6.1-bin-hadoop2.6/lib /spark
#
#ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
#ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
## update boot script
#COPY bootstrap.sh /etc/bootstrap.sh
#RUN chown root.root /etc/bootstrap.sh
#RUN chmod 700 /etc/bootstrap.sh
#
##install R
#RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
#RUN yum -y install R
#
##install python
#RUN yum install gcc openssl-devel bzip2-devel
#RUN cd /usr/src
#RUN wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
#RUN tar xzf Python-2.7.14.tgz
#RUN cd Python-2.7.15
#RUN ./configure --enable-optimizations
#RUN make altinstall
#
#
#ENTRYPOINT ["/etc/bootstrap.sh"]

#----------------------------------------------------------------------------------

#FROM bde2020/spark-submit:2.4.0-hadoop2.7
#
#MAINTAINER Cecile Tonglet <cecile.tonglet@tenforce.com>
#
#COPY template.sh /
#
## Copy the requirements.txt first, for separate dependency resolving and downloading
#ONBUILD COPY requirements.txt /app/
#ONBUILD RUN cd /app \
#      && pip3 install -r requirements.txt
#
## Copy the source code
#ONBUILD COPY . /app
#
#CMD ["/bin/bash", "/template.sh"]

#----------------------------------------------------------------------------------


FROM bde2020/spark-python-template:2.4.0-hadoop2.7

MAINTAINER You <you@example.org>

RUN pip install --upgrade pip
RUN pip install pyspark cassandra-driver

#ENV SPARK_APPLICATION_PYTHON_LOCATION /app/entrypoint.py
#ENV SPARK_APPLICATION_ARGS "foo bar baz"