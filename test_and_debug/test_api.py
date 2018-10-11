import requests
import json
import numpy as np
import pandas as pd
import os

# Use this to test locally
# BASE_URL = 'http://127.0.0.1:5000'

# Use this to test the heroku version
BASE_URL = 'https://hogwarts42-api-heroku.herokuapp.com'


# Train the model on the base dataset
print("**************** Training the model on the base Hogwarts dataset ****************")
response = requests.get("{}/train".format(BASE_URL))
print(response.text)
print('\n')



# Make a prediction: argmax P(y|X=x)
print("**************** Making a prediction with the Hogwarts model ****************")
data = json.dumps({'school':'hogwarts',
                    'astronomy': 800,
                    'herbology': -2,
                    'ancient_runes': 300})
response = requests.get("{}/predict".format(BASE_URL), json=data)
print(response.text)
print('\n')



# Transfer learning
print("**************** Training a new model for another wizards school, using transfer learning methods ****************")
dirname = os.path.dirname(__file__)
file_name = os.path.join(dirname,'polytechnique_dataset_transfer.csv')
data_set = pd.read_csv(file_name)

y = np.array(data_set['Hogwarts House'])
data_set.drop('Hogwarts House',axis=1,inplace=True)
X = np.array(data_set)


data = json.dumps({
    'school':'polytechnique',
    'regularization':{
        'method':None,
        'C':0
    },
    'optimizer':'sgd',
    'optimizer_params':{
        'alpha':0.1,
        'n':3,
        'batch_size':40
    },
    'X':X.tolist(),
    'y':y.tolist()
})

response = requests.get("{}/transfer".format(BASE_URL), json=data)
print(response.text)
print('\n')



# Make a prediction with the new model: argmax P(y|X=x)
print("**************** Making a prediction with the new model ****************")
data = json.dumps({'school':'polytechnique',
                    'astronomy': 800,
                    'herbology': -2,
                    'ancient_runes': 300})
response = requests.get("{}/predict".format(BASE_URL), json=data)
print(response.text)
print('\n')