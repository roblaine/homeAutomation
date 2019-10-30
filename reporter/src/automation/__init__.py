# initialise the db connection
import sqlalchemy
from sensors.sensor import Sensor
from gpiozero import PWMLED
from time import sleep


# factor by which to calibrate the real temp from raw temp by
FACTOR = 6.0
db = sqlalchemy.engine.create_engine('sqlite:///database.db', echo=True)
s = Sensor(FACTOR)

print('DB: %s' %(db.engine))

def main():
    led = PWMLED(17)
    
    for i in range(0,10):
        led.value = 0
        sleep(5)
        led.value=0.5
        sleep(5)
        led.value=1
        sleep(25)
    pass #implement

if __name__ == '__main__':
    main()
