import os, time, glob
from datetime import datetime

# Set up the temperature sensors
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Cloud SQL Connection details
CLOUD_SQL_ADDR='35.189.31.37'
CLOUD_SQL_USERNAME='raspberry-pi'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return datetime.now().strftime('%s'), temp_c

def save_to_cloudsql():
    data = read_temp()
    print(format('Saving data, {}, to cloud sql.', data))


if __name__ == '__main__':
    print(read_temp())

