#!/bin/bash
source /usr/src/app/Crawler/venv/bin/activate
exec gunicorn -c "/usr/src/app/Crawler/gunicorn_config.py" Crawler.wsgi
