#!/usr/bin/env bash

docker build --force-rm -t weather_sensor_alpine .
docker run \
	-it \
	--mount type=bind,source=`pwd`/tests/devices/,target=/devices \
	weather_sensor_alpine
