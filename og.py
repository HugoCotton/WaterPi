import requests
import calendar
import configparser
import json
import datetime
import os
import sys
import time
import math

from time import sleep

#get weatherhistory

weatherhistory = requests.get('http://api.openweathermap.org/data/2.5/onecall?lat=51.429968&lon=-0.200869&units=metric&appid=b8556c7b63a5627a09ec360f30809f6e')
weather_data = json.loads(weatherhistory.content.decode('utf-8'))
current_temp = weather_data["current"]["temp"]
print(weather_data[""])
print('The current temperature in Wimbledon, London is ',math.trunc(current_temp),'°C')



