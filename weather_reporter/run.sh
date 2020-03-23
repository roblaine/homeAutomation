
# Initaialise the modules
#modprobe w1-gpio
#modprobe w1-therm


docker build --force-rm -t weather_sensor_alpine .
docker run \
	-it \
	--mount type=bind,source=`pwd`/tests/devices/,target=/sensors \
	weather_sensor_alpine

