FROM python:3.8-alpine

LABEL maintainer="Container Solutions <info@container-solutions.com>"

# Install basic dependencies
RUN apk add -U curl git parallel

# Silence parallel citation notice
RUN mkdir /root/.parallel && \
    touch /root/.parallel/will-cite

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py | python

# Install grafanalib
RUN pip install grafanalib

WORKDIR /opt/code

CMD ["/bin/sh", "-c"]
