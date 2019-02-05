# import requests
# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Rennes,fr&APPID=')
# data = r.json()
# print(data)

import pyowm

owm = pyowm.OWM('58750219130143b7987aa6c46cae85f8')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Rennes, Fr')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

observation_list = owm.weather_around_coords(48.117266, -1.6777926)
