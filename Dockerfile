FROM python:3.8

RUN apt-get update -y && apt-get install -y gettext cron

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir -p /var/log/karino

COPY . .

ENV PYTHONUNBUFFERED 1

ENV PORT 8000
EXPOSE 8000
