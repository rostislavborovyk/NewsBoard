#!/bin/sh

#gunicorn -b 0.0.0.0:8000 news_board.wsgi
uwsgi --http :$PORT --wsgi-file news_board/wsgi.py  # faster option than gunicorn
