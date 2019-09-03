FROM python:3.7.4-alpine3.10
RUN apk add build-base make
ENV FLASK_APP=run.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["make", "docker_run"]