#!/usr/bin/sh

docker_output=$(echo -n `docker ps -aq`|sed -e 's/\s//g')
if [ ! $docker_output = *_"679ae1113896"_* ]; then
	echo "Yes";
fi

