import pandas as pd
import os
import numpy as np

dirname = os.path.dirname(__file__)
dirname = os.path.abspath(os.path.join(dirname, os.pardir))
dirname = os.path.join(dirname,'model')
dirname = os.path.join(dirname,'resources')
file_name = os.path.join(dirname,'dataset_train.csv')

data_set = pd.read_csv(file_name)
data_set.drop(['Index','First Name','Last Name','Birthday','Best Hand','Arithmancy',
               'Defense Against the Dark Arts','Divination','Muggle Studies','History of Magic',
               'Transfiguration','Potions', 'Care of Magical Creatures','Charms','Flying'], axis=1, inplace=True)
data_set[['Astronomy', 'Herbology', 'Ancient Runes']] = data_set[['Astronomy','Herbology','Ancient Runes']].fillna(data_set[['Astronomy','Herbology','Ancient Runes']].mean(axis=0))


data_set['Astronomy'] = data_set['Astronomy'].apply(lambda x: x*np.random.uniform(1.0,1.05))
data_set['Herbology'] = data_set['Herbology'].apply(lambda x: x*np.random.uniform(1.0,1.05))
data_set['Ancient Runes'] = data_set['Ancient Runes'].apply(lambda x: x*np.random.uniform(1.0,1.05))


dirname = os.path.dirname(__file__)
file_name = os.path.join(dirname,'polytechnique_dataset_transfer.csv')
data_set.to_csv(file_name,index=False)



print('!! Done !!')
