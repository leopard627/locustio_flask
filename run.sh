#!/bin/sh

gunicorn flaskr:app -w 16 --log-file ./gunicorn.log --log-level DEBUG
