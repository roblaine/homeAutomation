import os, time, glob
from datetime import datetime
import config
import db.database as db


# TODO: Refactor this as a class
# Set up the temperature sensors
if config.ENV == 'production':
  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')

  base_dir = '/sys/bus/w1/devices/'
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
