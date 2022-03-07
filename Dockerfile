FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    vim

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip \
    pip install -r requirements.txt