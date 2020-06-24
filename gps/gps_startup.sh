#!/bin/bash

gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
stty -F /dev/ttyUSB0 -echo
systemctl stop gpsd.socket
systemctl disable gpsd.socket
killall gpsd
systemctl stop gpsd.socket
systemctl disable gpsd.socket
gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock 
sleep 10s
nohup python sendCoordinate.py > pylog.test &

