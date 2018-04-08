#!/bin/bash

#OLD_HOST=$(hostname)
#NEW_HOST='ePhotoFrame'

#read -p "Change hostname? [Y/n]" -n 1 -r
#if [[ $REPLY =~ ^[Yy]$ ]]
#then
#	sudo sh -c "echo $NEW_HOST > /etc/hostname"
#	sudo sed -i "s/$OLD_HOST/$NEW_HOST/g" /etc/hosts
#	printf "\nHostname set!"
#fi

#echo ""

sudo apt-get install git imagemagick python-dev python-pip python-imaging build-essential -y --no-install-recommends


sudo pip install -v --upgrade pip setuptools
#sudo pip install -v --no-cache-dir pillow PyDispatcher Flask Flask-SocketIO flask_uploads gevent psutil python-dispatch eventlet greenlet bokeh


