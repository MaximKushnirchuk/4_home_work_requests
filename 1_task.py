'''Задача №1
Кто самый умный супергерой?
Есть API по информации о супергероях с информацией по всем супергероям. Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.'''

import json
import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
if 200 <= response.status_code < 300 :
    resp_dict = response.json()
max_intelligence = None
null_intel = 0
for hero in resp_dict :
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos' :
        if hero['powerstats']['intelligence'] > null_intel :
            null_intel = hero['powerstats']['intelligence']
            max_intelligence = hero['name']
print(f'Самый умный супергерой это - {max_intelligence}')

