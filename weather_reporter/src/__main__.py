from glob import glob
from config import *
from datetime import datetime as dt
from time import sleep
import os
import requests

from temp_sense.file_based_sensor import FileBasedSensor as fbs


def run():
    sensors_path = '/devices/**'

    if RUNNING_IN_CONTAINER == 'False':
        sensors_path = '/sys/bus/w1/devices/**'

    sensors_glob = glob(sensors_path)
    print(sensors_glob)

    sensors = []
    for sensor_path in sensors_glob:
        sensor_id = sensor_path.split('devices/')[1]
        sensors.append(fbs('Bedroom', sensor_id, sensor_path + '/w1_slave'))

    for sensor in sensors:
        print(sensor.read_temp())


# TODO: Use the sensor ID in the database entry
# bedroom_temp = fbs('Bedroom', 'DS18B20', '/sensors/28-00000000000000/w1_slave')
#
# def run():
#     # Log the current temperature into the database
#     curr_temp = bedroom_temp.read_temp()
#     timestamp = dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')
#
#     # Send the date to the server for processing
#     new_temp_ep = '/temps/new'
#     url = SERVER + new_temp_ep
#     print(url)
#
#     payload = {'temperature': curr_temp,
#             'location': bedroom_temp.get_name(),
#             'recorded_at': timestamp}
#
#     r = requests.post(url, data=payload)
#
#     print(r.json(), r.status_code)

if __name__ == '__main__':
  run()
