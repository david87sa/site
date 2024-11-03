#!/bin/sh
echo "start"
./start.sh
cp /code/site/sitesproject/sites /etc/nginx/sites-enabled/sites
ln -s /etc/nginx/sites-available/sites /etc/nginx/sites-enabled/sites
touch /run/openrc/softlevel
rc-service nginx start