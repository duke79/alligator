#!/usr/bin/env bash

## Copyright 2015 Google Inc.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
#
## [START startup]
#set -v
#
## Talk to the metadata server to get the project id
#PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
#
## Install logging monitor. The monitor will automatically pickup logs sent to
## syslog.
## [START logging]
#curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
#service google-fluentd restart &
## [END logging]
#
## Install dependencies from apt
#apt-get update
#apt-get install -yq \
#    git build-essential supervisor python python-dev python-pip libffi-dev \
#    libssl-dev
#
## Create a pythonapp user. The application will run as this user.
#useradd -m -d /home/pythonapp pythonapp
#
## pip from apt is out of date, so make it update itself and install virtualenv.
#pip install --upgrade pip virtualenv
#
## Get the source code from the Google Cloud Repository
## git requires $HOME and it's not set during the startup script.
#export HOME=/root
#git config --global credential.helper gcloud.sh
#git clone https://source.developers.google.com/p/$PROJECTID/r/[YOUR_REPO_NAME] /opt/app
#
## Install app dependencies
#virtualenv -p python3 /opt/app/7-gce/env
#source /opt/app/7-gce/env/bin/activate
#/opt/app/7-gce/env/bin/pip install -r /opt/app/7-gce/requirements.txt
#
## Make sure the pythonapp user owns the application code
#chown -R pythonapp:pythonapp /opt/app
#
## Configure supervisor to start gunicorn inside of our virtualenv and run the
## application.
#cat >/etc/supervisor/conf.d/python-app.conf << EOF
#[program:pythonapp]
#directory=/opt/app/7-gce
#command=/opt/app/7-gce/env/bin/honcho start -f ./procfile worker bookshelf
#autostart=true
#autorestart=true
#user=pythonapp
## Environment variables ensure that the application runs inside of the
## configured virtualenv.
#environment=VIRTUAL_ENV="/opt/app/7-gce/env",PATH="/opt/app/7-gce/env/bin",\
#    HOME="/home/pythonapp",USER="pythonapp"
#stdout_logfile=syslog
#stderr_logfile=syslog
#EOF
#
#supervisorctl reread
#supervisorctl update
#
## Application should now be running under supervisor
## [END startup]



sudo apt-get install curl
sudo apt-get install wget
sudo apt-get install python-pip
#pip fix 1 : update pip
# pip install -U pip
#pip fix 2 : update python
# sudo apt-get upgrade python #Only if pip doesn't work
#pip fix 3 : Alternate pip installation
#wget https://pypi.python.org/packages/e7/a8/7556133689add8d1a54c0b14aeff0acb03c64707ce100ecd53934da1aa13/pip-8.1.2.tar.gz
#tar -xzvf pip-8.1.2.tar.gz
#cd pip-8.1.2
#sudo python setup.py install

## Python 3.6
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

## Python 3.6 - alternative 1
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.4 #3.6 might not be strictly required

sudo pip install pipenv --skip-lock #try sudo if fails, and --python <path_to_python) if required
sudo apt-get install git
#git clone <path_to_repo>

sudo apt-get install nginx

##Launch
sudo bash RunServer.sh

### Cloud SQL
gcloud sql connect instance-1 --user=root










###Only for local linux machine, not for gcloud
sudo apt-get update && sudo apt-get upgrade
# For putty access from windows
sudo apt-get install openssh-server #https://askubuntu.com/questions/136671/how-to-login-into-a-ubuntu-machine-from-windows
ip route get 8.8.8.8 | awk '{print $NF; exit}' #https://askubuntu.com/questions/430853/how-do-i-find-my-internal-ip-address

##MySQL
sudo apt-cache search mysql | grep mysql-server | more
#sudo apt-get install mysql-server
https://dev.mysql.com/downloads/mysql/ #download deb
https://askubuntu.com/questions/753716/how-to-install-mysql-5-6-19
#wget https://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb
#sudo dpkg -i downloaded_deb
sudo dpkg -i mysql-common_8.0.12-1ubuntu16.04_i386.deb
sudo dpkg-preconfigure mysql-community-server_8.0.12-1ubuntu16.04_i386.deb
sudo apt-get install libaio1
sudo dpkg -i mysql-community-server_8.0.12-1ubuntu16.04_i386.deb
sudo dpkg -i mysql-community-client_8.0.12-1ubuntu16.04_i386.deb
sudo dpkg -i libmysqlclient21_8.0.12-1ubuntu16.04_i386.deb
sudo apt-get update
sudo apt-get install mysql-server-5.6
sudo service mysql start
mysql -u root -p
#CREATE USER 'vilokanlabs'@'192.168.1.101' IDENTIFIED BY 'Dynamic.123';
CREATE USER 'vilokanlabs'@'%' IDENTIFIED BY 'Dynamic.123';
GRANT ALL PRIVILEGES ON *.* TO 'vilokanlabs'@'192.168.%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE alligator;

#Right ctrl + c # To get out of scaled view mode

##Share folder
#enable vboxsf #https://superuser.com/questions/496513/mount-gives-unknown-filesystem-type-vboxsf
#share folder #https://www.youtube.com/watch?v=ddExu55cJOI
sudo mount -t vboxsf Dev /home/duke79/SharedWindows

##Network
#access ip #https://stackoverflow.com/questions/11177809/how-to-ping-ubuntu-guest-on-virtualbox
#change to static (step 3) #https://websiteforstudents.com/switch-static-ip-address-ubuntu-17-04-17-10/

#Hidden folders
#https://askubuntu.com/questions/470837/how-to-show-hidden-folders-in-ubuntu-14-04


##Add category
#http://192.168.1.102/graph
curl -X POST  http://192.168.1.102/graph -H "ontent-type: multipart/form-data;" -F "query={ categories(action: {add: {title: \"news\"}}) {  title }}"

##Populate db
export PYTHONPATH="${PYTHONPATH}:/home/duke79/SharedWindows/alligator/src/flask/"
pipenv run python scripts/create_db_schema.py
pipenv run python scripts/populate_db.py
mysql -u root -p
USE alligator;
SHOW TABLES; #Check db

