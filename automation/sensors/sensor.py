# sensor file for controlling the gathering of environmental data.  
#from sense_hat import SenseHat 


class Sensor():
    def __init__(self, factor):
        #self.sense = SenseHat()
        self.factor = factor

    def getRawTemp(self):
        """Returns the current temperature"""
        #return self.sense.get_temperature()
        pass

    #def calibrateTemp(self, temp):
    #    """Calculates the calibrated real temperature""" 
    #   return (getRawTemp() - temp)


