!#/usr/bin/env/bash

# Initaialise the modules
modprobe w1-gpio
modprobe w1-therm

docker run \
	--mount type=bind,source=/sys/bus/w1/devices/,target=/sensors \
	weather-alpine
