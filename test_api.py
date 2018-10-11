import requests
import json


BASE_URL = 'http://127.0.0.1:5000'



# Train the model on the base dataset
response = requests.get("{}/train".format(BASE_URL))
print(response.text)



# Make a prediction: argmax P(y|X=x)
data = json.dumps({'school':'hogwarts',
                    'astronomy': 800,
                    'herbology': -2,
                    'ancient_runes': 300})
response = requests.get("{}/predict".format(BASE_URL), json=data)
print(response.text)