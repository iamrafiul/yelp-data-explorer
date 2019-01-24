FROM bde2020/spark-python-template:2.4.0-hadoop2.7

MAINTAINER You <you@example.org>

RUN chmod 777 /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

