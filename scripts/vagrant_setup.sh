#!/bin/bash

PICOCTF_HOME=${PICOCTF_HOME:-'/home/vagrant/'}

# Updates
apt-get -y update
apt-get -y upgrade

# CTF-Platform Dependencies
apt-get -y install python3-pip
apt-get -y install nginx
apt-get -y install mongodb
apt-get -y install gunicorn
apt-get -y install git
apt-get -y install libzmq-dev
apt-get -y install nodejs-legacy
apt-get -y install npm
apt-get -y install libclosure-compiler-java
apt-get -y install ruby-dev
apt-get -y install dos2unix
apt-get -y install tmux
apt-get -y install openjdk-7-jdk

npm install -g coffee-script
npm install -g react-tools
npm install -g jsxhint

pip3 install -r ${PICOCTF_HOME}/api/requirements.txt

# Jekyll
gem install jekyll -v 2.5.3

# Configure Environment
echo 'PATH=$PATH:${PICOCTF_HOME}/scripts' >> /etc/profile

# Configure Nginx
cp ${PICOCTF_HOME}/config/ctf.nginx /etc/nginx/sites-enabled/ctf
rm /etc/nginx/sites-enabled/default
mkdir -p /srv/http/ctf
service nginx restart
