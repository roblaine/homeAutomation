# sensor file for controlling the gathering of environmental data.  
from sense_hat import SenseHat 
import numpy


class Sensor():
    this.sense = None
    this.constant = None

    def __init__(self, constant):
        this.sense = SenseHat()
        this.constant = constant

    def getRawTemp(self):
        this.sense.get_temperature()
    
    def calibrateTemp(self, temp):
        return getRawTemp() - temp

