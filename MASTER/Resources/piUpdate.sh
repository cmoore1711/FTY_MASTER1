#!/bin/sh

cd Desktop/FTY_MASTER1/MASTER
sudo git pull
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install rdate
sudo apt-get -purge remove xscreensaver
