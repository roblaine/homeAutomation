# sensor file for controlling the gathering of environmental data.  
from sense_hat import SenseHat 


class Sensor():
    self.sense = None
    self.constant = None

    def __init__(self, constant):
        self.sense = SenseHat()
        self.constant = constant

    def getRawTemp(self):
        self.sense.get_temperature()
    
    def calibrateTemp(self, temp):
        return getRawTemp() - temp

