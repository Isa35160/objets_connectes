import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Rennes,fr&APPID=58750219130143b7987aa6c46cae85f8')
data = r.json()
print(data)
