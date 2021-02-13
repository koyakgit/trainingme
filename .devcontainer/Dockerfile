# For development by VSCode

# Base image is debian
FROM python:3.8.2-alpine3.11
LABEL Name=kk Version=0.0.1

# Localize
RUN apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*
# Set the lang, you can also specify it as as environment variable through docker-compose.yml
ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8

# Install Git
RUN apk add git curl lsof

# update pip to latest
RUN pip install --upgrade pip && \
    pip install --upgrade flake8 autopep8 && \
    pip install --upgrade gunicorn && \
    pip install --upgrade ptvsd && \
    pip install requests luigi flask SQLAlchemy

EXPOSE 5000
