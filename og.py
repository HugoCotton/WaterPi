import requests
import calendar
import configparser
import json
import datetime
import os
import sys
import time
import math
import xml.etree.ElementTree as ET

from time import sleep

#get weatherdata

weather_data = requests.get('http://api.weatherapi.com/v1/forecast.json?key=4ab9e3a07045457d80c144348211310&q=SW19&days=10&aqi=no&alerts=no')
weather_data = weather_data.json()

def getcurrenttemp():
    current_data = weather_data["current"]
    current_temp = current_data["temp_c"]
    return current_temp

def getcurrentprecip():
    current_data = weather_data["current"]
    current_precip = current_data["precip_mm"]
    return current_precip

def current_highs():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    max_temp = forecast_day[0]['day']['maxtemp_c']
    return max_temp

def current_lows():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    min_temp = forecast_day[0]['day']['mintemp_c']
    return min_temp

def rain_chance():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    rain_chance = forecast_day[0]['day']['daily_chance_of_rain']
    return rain_chance

def rain_chance():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    total_precip = forecast_day[0]['day']['totalprecip_mm']
    return total_precip

def rain_tomorrow():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    rain_chance_tomorrow = forecast_day[1]['day']['daily_chance_of_rain']
    return rain_chance_tomorrow

def next_rain():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    for i in range(len(forecast_day)):


def likelihood(value):
    if value >= 75:
        return 'high'
    elif value < 75 and value >= 50:
        return 'medium'
    elif value < 50 and value >= 25:
        return 'low'
    elif value < 25 and value > 0:
        return 'very low'
    elif value == 0:
        return '0%'

def snow():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    snow = forecast_day[0]['day']['daily_will_it_snow']
    chance_snow = forecast_day[0]['day']['daily_chance_of_snow']
    if snow == 1:
        return True
    else:
        pass

def chance_snow():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    chance_snow = forecast_day[0]['day']['daily_chance_of_snow']
    return chance_snow


print(f'The current temperature in Wimbledon, London is {getcurrenttemp()}°C')
print(f'Today, you can expect highs of {current_highs()}°C and lows of {current_lows()}°C')


if getcurrentprecip() > 0:
    print(f'There is currently {getcurrentprecip()}mm of rain')
else:
    print(f'There is a {likelihood(rain_chance())} chance of rain today')

###################################################################################

if rain_tomorrow() > 0:    
    print(f'There is a {likelihood(rain_tomorrow())} chance of rain tomorrow')
else:
    print(f'It will rain next in {next_rain()} days')

###################################################################################

if snow() == True:
    print(f'It may snow today! There is a {likelihood(chance_snow())} chance of snow')

