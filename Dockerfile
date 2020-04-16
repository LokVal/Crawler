FROM python:3-alpine

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN export DJANGO_SETTINGS_MODULE=Crawler.settings
RUN source venv/bin/activate
RUN venv/bin/pip3 install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "Crawler.wsgi", "0:8000"]
