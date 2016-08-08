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

EXPOSE 5000

CMD ["python", "run.py"]