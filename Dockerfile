FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    vim

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY . /app/