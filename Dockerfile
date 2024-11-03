FROM python:3.9-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
# Allows docker to cache installed dependencies between builds
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . /code

EXPOSE 80



RUN apk add git
RUN rm -rf site
RUN git clone https://github.com/david87sa/site.git

COPY sitesproject/sitesproject/settings-prod.py /code/site/sitesproject/sitesproject/settings.py

WORKDIR /code/site/sitesproject/
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 "
#CMD ["python", "manage.py", "migrate"]

COPY gunicorn/start.sh .
COPY setup.sh /code/site/sitesproject/setup.sh
RUN chmod +x start.sh
RUN chmod +x /code/site/sitesproject/setup.sh


RUN apk add nginx
RUN apk add openrc --no-cache


CMD ["/code/site/sitesproject/setup.sh"]