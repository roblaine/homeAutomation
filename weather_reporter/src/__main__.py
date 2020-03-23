from glob import glob
from config import *
from datetime import datetime as dt
from time import sleep
from datetime import datetime
import os
import requests

from temp_sense.file_based_sensor import FileBasedSensor as fbs


def run():
    sensors_path = '/devices/**'

    if RUNNING_IN_CONTAINER == 'False':
        sensors_path = '/sys/bus/w1/devices/**'

    sensors_glob = glob(sensors_path + '28**')
    print(sensors_glob)

    sensors = []
    for sensor_path in sensors_glob:
        sensor_id = sensor_path.split('devices/')[1]
        sensors.append(fbs('Bedroom', sensor_id, sensor_path + '/w1_slave'))

    for sensor in sensors:
        # POST data to the server /temps/new endpoint
        temperature = sensor.read_temp()
        recorded_at = datetime.utcnow().strftime('%Y-%M-%d %H:%m:%S')
        payload = {
                'temperature': temperature,
                'sensor_id': sensor.s_id,
                'location': sensor.get_name(),
                'recorded_at': recorded_at}

        # Send the date to the server for processing
        new_temp_ep = '/temps/new'
        url = SERVER + new_temp_ep
        print(url)

        r = requests.post(url, data=payload)
        print(r.json())

if __name__ == '__main__':
  run()
