FROM ubuntu:16.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3.4 python-pip mysql-client-core-5.5

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ADD . /usr/src/app

ADD script.sh /usr/src/app/script.sh
RUN chmod +x script.sh

ENV MYSQL_HOST=db1.cziojw5wy8sn.us-west-2.rds.amazonaws.com
ENV MYSQL_USER=harsh
ENV MYSQL_PASSWORD=secretpass
ENV MYSQL_DATABASE=mydb

EXPOSE 5000

ENTRYPOINT ["./script.sh", "db1.cziojw5wy8sn.us-west-2.rds.amazonaws.com", "harsh", "secretpass"]
