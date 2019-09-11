# module for querying the weather api's for forecasts and predictions
import requests
import json


class Weather():
    '''Class for queryiong the api endpoint at openweather.org'''
    def __init__(self,country_code,city,api_key):
        self.country_code = country_code
        self.city = city
        self.api_key = api_key
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=melbourne,au&appid=' + self.api_key
    
    def get_weather(self):
        '''Retrieve the weather from a number of api's'''
        req = requests.get(self.weather_url)
        
        if not req.ok:
           # request failed, return None so we can catch this later
           return None

        # request was ok, convert it to json to get the data that we need
        req = req.json()
        print("\n%s\n"  % (req))
        weather = {} 
        weather['description'] = req['weather'][0]['description']
        # weather data is stored as a value in Kelvin (K)
        weather['values'] = req['main']
        # return the crucial info from the weather object
        return weather
    
    def kelvin_to_cent(self,tempK):
        '''Convert the temperature in kelvin to the equivalent 
        in celsius'''
        return tempK + 273.15

    def save_latest_call(self):
        '''Save the latest weather api call into our database'''
        pass

    def retrieve_latest_data(self):
        '''Retrieve the latest saved data from our database.'''
        pass


