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
        #req = requests.get(self.weather_url).json()
        req = json.loads('{"coord": {"lon": 144.96, "lat": -37.81}, "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}], "base": "stations", "main": {"temp": 291.82, "pressure": 1006, "humidity": 88, "temp_min": 291.15, "temp_max": 293.15}, "visibility": 10000, "wind": {"speed": 2.1, "deg": 50}, "clouds": {"all": 75}, "dt": 1544787240, "sys": {"type": 1, "id": 9554, "message": 0.0034, "country": "AU", "sunrise": 1544727125, "sunset": 1544780265}, "id": 2158177, "name": "Melbourne", "cod": 200}')
        #if not req.ok():
        #   # request failed, return None so we can catch this later
        #   return None
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


