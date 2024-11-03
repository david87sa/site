#!/bin/bash

NAME="sites"                                  # Name of the application
DJANGODIR=/code/sites/sitesproject             # Django project directory
SOCKFILE=/code/sites/sitesproject/run/gunicorn.sock  # we will communicte using this unix socket
                # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn sitesproject.wsgi:application \
  --name $NAME \
  --bind=unix:$SOCKFILE \
  --log-level=info \
  --log-file=-