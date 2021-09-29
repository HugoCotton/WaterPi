#weather API test

import requests
import calendar
import configparser
import json
import datetime
import os
import sys

from time import sleep

def getconfig(filename='config'):
    config = configparser.RawConfigParser()
    this_dir = os.path.abspath(os.path.dirname(__file__))
    config.read(this_dir + '/' + filename)
    if config.has_section('WaterPi Config'):
        return {name:val for (name, val) in config.items('WaterPi Config')}
    else:
        print('Error: Unable to find or read WaterPi Config file')

def getweatherhistory(config, timestamp_dt):
    API_URL = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={day}&appid={key}'
    weatherhistory = requests.get(API_URL.format(key=config['api_key'], 
                                    day = timestamp_dt,
                                    lat = config['lat'],
                                    lon = config['lon']))
    weather_data = json.loads(weatherhistory.content.decode('utf-8'))
    hourly_rain = {x.get('dt'): x.get('rain').get('1h') for x in weather_data.get('hourly') if x.get('rain') and x.get('dt') >= timestamp_dt}
    return hourly_rain

def get_weather(config, timestamp_dt):
    API_URL = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&dt={day}&appid={key}'
    weather_today = requests.get(API_URL.format(key=config['api_key'],
                                    day=timestamp_dt,
                                    lat=config['lat'],
                                    lon=config['lon']))
    weather_data = json.loads(weather_today.content.decode('utf-8'))
    curr_rain = {}  
    curr = weather_data.get('current')

    if curr:
        rain = curr.get('rain', 0)
        if rain:
            curr_rain = {timestamp_dt: rain.get('1h', 0)}

    hourly_rain = {x.get('dt'): x.get('rain').get('1h') for x in weather_data.get('hourly') if x.get('rain') and x.get('dt') < timestamp_dt}
    hourly_rain.update(curr_rain)
    return hourly_rain

print(timestamp_dt)
