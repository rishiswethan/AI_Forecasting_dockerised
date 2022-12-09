FROM python:3.10.8-slim

RUN apt-get -y update && apt-get install -y \
    dos2unix \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY ./docker_app/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


RUN mkdir -p /usr/docker_app
# RUN mkdir -p /opt/ml_vol
WORKDIR /usr/docker_app/
COPY ./docker_app .
# RUN python setup.py

ENV PATH="/usr/docker_app:${PATH}"
RUN dos2unix train &&\
    dos2unix test &&\
    dos2unix predict &&\
    dos2unix tune

RUN chmod +x train &&\
    chmod +x test &&\
    chmod +x predict &&\
    chmod +x tune

RUN apt remove -y dos2unix\
    vim