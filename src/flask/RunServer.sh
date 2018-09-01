#!/usr/bin/env bash

#http://docs.gunicorn.org/en/stable/design.html
#https://stackoverflow.com/questions/15979428/what-is-the-appropriate-number-of-gunicorn-workers-for-each-amazon-instance-type/27664071#27664071
pipenv run gunicorn run:app -b 192.168.1.102:5000 -w $(( 2 * `cat /proc/cpuinfo | grep 'core id' | wc -l` + 1 ))
#pipenv run python run.py
