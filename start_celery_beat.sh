#!/bin/bash
source /usr/src/app/Crawler/venv/bin/activate
exec ../celery -A product_parser beat --loglevel=info
