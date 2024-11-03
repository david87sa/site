#!/bin/sh

NAME="sites"                                  # Name of the application
DJANGODIR=/code/site/sitesproject             # Django project directory
SOCKFILE=/code/site/sitesproject/run/gunicorn.sock  # we will communicte using this unix socket
                # WSGI module name
mkdir /code/site/sitesproject/run/
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn sitesproject.wsgi:application \
  --name $NAME \
  --bind=unix:$SOCKFILE \
  --log-level=info \
  --log-file=-