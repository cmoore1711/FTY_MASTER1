#!/bin/sh

cd Desktop/FTY_MASTER1/MASTER
sudo git pull

sudo apt-get install rdate
sudo apt-get -y remove xscreensaver
sudo /etc/init.d/ntp stop
sudo /etc/init.d/ntp start

