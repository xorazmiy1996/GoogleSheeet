FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN mkdir /app/staticfiles
RUN mkdir /app/media

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libpq-dev

RUN pip install pipenv && pipenv install --system

COPY scripts/entrypoint.sh .
COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]