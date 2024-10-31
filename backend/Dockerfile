FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/django-entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/bin/sh", "/app/django-entrypoint.sh" ]