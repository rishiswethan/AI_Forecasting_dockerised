FROM python:3.10.8

COPY ./docker_app/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


RUN mkdir -p /usr/docker_app
WORKDIR /usr/docker_app/
COPY ./docker_app .
RUN python setup.py
