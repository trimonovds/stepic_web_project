#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
cd /home/box/web/
sudo gunicorn --config='/etc/gunicorn.d/hello.py' hello:app &
cd ask/
sudo gunicorn -b :8000 ask.wsgi:application &