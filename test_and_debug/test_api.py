import requests
import json
import numpy as np


BASE_URL = 'http://127.0.0.1:5000'


"""
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

"""

# Transfer learning
data = json.dumps({
    'school':'polytechnique',
    'regularization':{
        'method':'l2',
        'C':0.75
    },
    'optimizer':'sgd',
    'optimizer_params':{
        'alpha':0.01,
        'n':5,
        'batch_size':14
    },
    'X':np.array([[1,2,2],[1,3,1],[1,5,6],[1,4,7]]).tolist(),
    'y':np.array(["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]).tolist()
})

response = requests.get("{}/transfer".format(BASE_URL), json=data)
print(response.text)