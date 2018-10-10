import requests
import json


BASE_URL = 'http://127.0.0.1:5000'


data = json.dumps({'school':'hogwarts',
                    'astronomy': 102,
                    'herbology': 140,
                    'ancient_runes': 10})

response = requests.get("{}/predict".format(BASE_URL), json=data)

print(response.text)