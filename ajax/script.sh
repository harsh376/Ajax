#!/bin/bash

cmd="python run.py"
host="$1"
port="3306"
user="$2"
password="$3"

while ! mysql -h"$host" -P"$port" -u"$user" -p"$password"  -e ";" ; do
    >&2 echo "Can't connect, please retry"
    sleep 1
done

>&2 echo "MYSQL is up - executing command"
exec $cmd
