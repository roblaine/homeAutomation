# initialise the db connection
#from sqlalchemy import SQLAlchemy
from automation.sensors.sensor import Sensor


# factor by which to calibrate the real temp from raw temp by
FACTOR = 6.0
#db = sqlalchemy.engine.create_engine('sqlite:///database.db', echo=True)
s = Sensor(FACTOR)

#print('DB: %s' %(db.engine))

def main():
    pass #implement

if __name__ == '__main__':
    main()
