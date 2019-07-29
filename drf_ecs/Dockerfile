FROM python:3.6-alpine

WORKDIR /usr/src/drf_ecs
COPY requirements.txt ./

RUN apk update

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD python manage.py runserver 0.0.0.0:8080