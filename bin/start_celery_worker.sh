#!/bin/bash
source /usr/src/app/Crawler/venv/bin/activate
exec ../celery -A product_parser worker --loglevel=info
