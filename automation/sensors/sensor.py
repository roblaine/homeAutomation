# sensor file for controlling the gathering of environmental data.  
from sense_hat import SenseHat 


class Sensor():
    def __init__(self, constant):
        self.sense = SenseHat()
        self.constant = constant

    def getRawTemp(self):
        self.sense.get_temperature()
    
    def calibrateTemp(self, temp):
        return getRawTemp() - temp

