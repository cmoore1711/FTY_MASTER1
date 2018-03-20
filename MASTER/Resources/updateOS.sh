#!/bin/sh


sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install rdate
sudo apt-get -y remove xscreensaver
sudo /etc/init.d/ntp stop
sudo /etc/init.d/ntp start
