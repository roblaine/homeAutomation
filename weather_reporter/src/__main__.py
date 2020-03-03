import config
import requests
from datetime import datetime as dt
from time import sleep

from temp_sense.file_based_sensor import FileBasedSensor as fbs


bedroom_temp = fbs('Bedroom', 'DS18B20', '/sensors/28-00000000000000/w1_slave')

def run():
    # Log the current temperature into the database
    curr_temp = bedroom_temp.read_temp()
    timestamp = dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Send the date to the server for processing


if __name__ == '__main__':
  run()
