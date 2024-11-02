FROM python:3.9-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
# Allows docker to cache installed dependencies between builds
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . /code

EXPOSE 8000



RUN apk add git
RUN rm -rf site
RUN git clone https://github.com/david87sa/site.git

WORKDIR site/sitesproject/
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 "
#CMD ["python", "manage.py", "migrate"]

CMD ["gunicorn","sitesproject.wsgi"]