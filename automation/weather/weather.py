# module for querying the weather api's for forecasts and predictions
import requests


class Weather():
    '''Class for queryiong the api endpoint at openweather.org'''
    def __init__(self,country_code,city,api_key):
        self.country_code = country_code
        self.city = city
        self.api_key = api_key
    
    def get_weather(self):
        '''Retrieve the weather from a number of api's'''
        pass

    def save_latest_call(self):
        '''Save the latest weather api call into our database'''
        pass

    def retrieve_latest_data(self):
        '''Retrieve the latest saved data from our database.'''
        pass


