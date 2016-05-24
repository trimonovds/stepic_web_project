#!/usr/bin/env bash
sudo ln -sf /home/bi/PycharmProjects/stepic_web_project/etc/nginx-test.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart