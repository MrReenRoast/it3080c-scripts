import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=557822906e3ff7c0288ac9d48baee0a4' % zip)
data=r.json()
print(data)
print(data['weather'][0]['description'])
