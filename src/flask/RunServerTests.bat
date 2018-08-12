@echo off
pipenv run python -m pytest
exit %errorlevel%
