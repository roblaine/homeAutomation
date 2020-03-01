import os, time, glob
from datetime import datetime
import config
import db.database as db


class ReadFileBasedSensor():
    """Class to read and record the value of a digital sensor such as the DS18B20.

        Reads from a filepath to return the contents of a file on disk that contains the data from the sensor.
    """
    def __init__(self, name, s_type, f_path):
        self.name = name
        self.s_type = s_type
        self.f_path = f_path

    def set_path(self, f_path):
        self.f_path = f_path

    def read_raw_value(self):
        """Reads the raw value of the sensor and returns the lines from the file"""
        with open(self.f_path, 'r') as sensor:
            return sensor.readlines()

    def read_value(self):
        """Reads the value of the sensor
        """
        pass

    def format_data(self):
        """Formats the data so that it can be saved as a tuple
        """
        pass



# TODO: Refactor this as a class
# Set up the temperature sensors
if config.ENV == 'production':
  # Do this on the device
  # os.system('modprobe w1-gpio')
  # os.system('modprobe w1-therm')

  # TODO fix the logic to handle more than one device on line 15
  base_dir = '/sensors' # Volume mount this in docker run command '/sys/bus/w1/devices/'
  device_folder = glob.glob(base_dir + '28*')[0]
  device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  if config.ENV == 'production':
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      return datetime.now().strftime('%s'), temp_c, 'Living Room'
  else:
    return datetime.now().strftime('%s'), -999, 'Living Room'

def save_to_db(timestamp, temp_val, location):
  # Create the insert object
  ins = db.temperatures.insert().values(location=location,temperature=temp_val,time=timestamp)
  # Compile and insert a new entry
  ins.compile().params
  res = db.connection.execute(ins)
  # Print the obejct to confirm that it was inserted
  print(res)
