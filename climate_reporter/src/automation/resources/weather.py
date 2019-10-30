# module for getting weather reports, and estimating temparture for the day
import requests


class Weather():
    def __init__(self):
        """Class to find weather reports and interpret the data"""
        self.dt = None # daily temp
        self.dh = None # daily humidity
    def getWeather(self):
        """queries api for the weather and stores the information
        """
        return None
