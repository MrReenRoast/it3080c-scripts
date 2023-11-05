import json
import requests

r = requests.get('http://localhost:3000')
data=r.json()
for i in range(len(data)):
    print (f'{data[i]["name"]} is: {data[i]["color"]}')
