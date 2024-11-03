#!/bin/sh
echo "start"
./start.sh
cp /code/site/sitesproject/sites /etc/nginx/http.d/sites.conf
mkdir /code/site/logs/
rc-service nginx start
touch /run/openrc/softlevel
rc-service nginx start