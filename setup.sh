#!/bin/sh
echo "start"
./start.sh &
echo "configuring nginx"
cp /code/site/sitesproject/sites /etc/nginx/http.d/sites.conf
mkdir /code/site/logs/
echo "starting nginx"
nginx