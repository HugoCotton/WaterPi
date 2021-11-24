import requests
import pyglet

window = pyglet.window.Window()


#get weatherdata

weather_data = requests.get('http://api.weatherapi.com/v1/forecast.json?key=4ab9e3a07045457d80c144348211310&q=56.8199, -5.104&days=10&aqi=no&alerts=no')
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

def total_precip():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    total_precip = forecast_day[0]['day']['totalprecip_mm']
    return total_precip

def rain_tomorrow():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    rain_chance_tomorrow = forecast_day[0]['day']['daily_will_it_rain']
    return rain_chance_tomorrow

def next_rain():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    for i in range(len(forecast_day)):
        if forecast_day[i]['day']['daily_will_it_rain'] == 1:
            next_rain = i
            return next_rain
            break
        else:
            pass
        

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

def days_in_data():
    forecast_data = weather_data["forecast"]
    forecast_day = forecast_data["forecastday"]
    return len(forecast_day)

print(f'The current temperature in Wimbledon, London is {getcurrenttemp()}°C')
print(f'Today, you can expect highs of {current_highs()}°C and lows of {current_lows()}°C')


if getcurrentprecip() > 0:
    print(f'There is currently {getcurrentprecip()}mm of rain')
else:
    print(f'There is a {likelihood(rain_chance())} chance of rain today')

###################################################################################

if rain_tomorrow() > 0:    
    print(f'There is a {likelihood(rain_tomorrow())} chance of rain tomorrow')
elif next_rain() == None:
    print(f'It will not rain for the next {days_in_data()} days')
else:
    print(f'It will rain next in {next_rain()} days')

###################################################################################

if snow() == True:
    print(f'It may snow today! There is a {likelihood(chance_snow())} chance of snow')



locationname = pyglet.text.Label('Wimbledon, London',
                        font_name='Miller Display Light',
                        font_size=20,
                        x=window.width//2, y=window.height-window.height//4,
                        anchor_x='center', anchor_y='center')

welcome = pyglet.text.Label("Hello! Here's your weather report for:",
                        font_name='Miller Display Light',
                        font_size=20,
                        x=window.width//2, y=window.height-window.height//6,
                        anchor_x='center', anchor_y='center')

temperature = pyglet.text.Label(f'The current temperature is {getcurrenttemp()}°C',
                        font_name='Miller Display Light',
                        font_size=20,
                        x=window.width//2, y=window.height-(window.height//4)-50,
                        anchor_x='center', anchor_y='center')

high = pyglet.text.Label(f'The highs today are {current_highs()}°C',
                        font_name='Miller Display Light',
                        font_size=20,
                        x=window.width//2, y=window.height-(window.height//4)-80,
                        anchor_x='center', anchor_y='center')                        

image = pyglet.resource.image('blue2.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    locationname.draw()
    welcome.draw()
    temperature.draw()
    high.draw()

pyglet.app.run()