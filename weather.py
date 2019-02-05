import requests
r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=58750219130143b7987aa6c46cae85f8 ')
data = r.json()
print(data)
