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
        uid = sensor_path.split('devices/')[1]
        sensors.append(fbs('Bedroom', uid, sensor_path + '/w1_slave'))

    print(sensors)
    for sensor in sensors:
        # Look up the sensor id from the sensors table for the FK
        sensor_id = None
        lookup_payload = { 'uid': sensor.uid }

        lookup_ep = '/sensors'
        lookup_url = SERVER + lookup_ep

        # Get the sensor's data as a json response object
        lookup_response = requests.post(lookup_url,
            data=lookup_payload).json()
        print(lookup_response)

        # POST data to the server /temps/new endpoint
        temperature = sensor.read_temp()
        recorded_at = datetime.utcnow().strftime('%Y-%M-%d %H:%m:%S')
        temp_payload = {
                'temperature': temperature,
                'sensor_id': sensor_id,
                'location': sensor.get_name(),
                'recorded_at': recorded_at}

        # Send the date to the server for processing
        new_temp_ep = '/temps/new'
        temp_url = SERVER + new_temp_ep

        temp_response = requests.post(temp_url, data=temp_payload)
        print(temp_response.json())

if __name__ == '__main__':
  run()
