import requests
import json

lat, lon = 35.0927175, 128.9102836
API_key = "551fe3ce5e72766f1646a2528d5aa088"

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

response = requests.get(url).json()
k_temp = response['main']['temp']
temp = round(k_temp - 273.15,2)
description = response['weather'][0]['description']
print(f'캘빈 온도 : {k_temp}K')
print(f'섭씨 온도 : {temp}\'C')
print(f'날씨 설명 : {description}')