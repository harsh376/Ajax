#!/bin/bash

cmd="python run.py"

while ! mysql -h"192.168.99.100" -P"3306" -uroot -p"my-secret-pw"  -e ";" ; do
    >&2 echo "Can't connect, please retry"
    sleep 1
done


>&2 echo "MYSQL is up - executing command"
exec $cmd
