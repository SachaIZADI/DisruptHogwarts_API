from flask import Flask, jsonify, request
from model.logistic_regression import LogisticRegression
import numpy as np
import json

"""
- https://www.wintellect.com/creating-machine-learning-web-api-flask/
- https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
- https://github.com/Wintellect/DataScienceExamples/blob/master/Regression/SimpleLinearRegressionAPI.py
"""


app = Flask(__name__)


@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        try:
            try:
                data = json.loads(request.json)
                school = data['school']
                astronomy = float(data['astronomy'])
                herbology = float(data['herbology'])
                ancient_runes = float(data['ancient_runes'])
            except:
                data = request.args
                school = data.get('school')
                astronomy = float(data.get('astronomy'))
                herbology = float(data.get('herbology'))
                ancient_runes = float(data.get('ancient_runes'))




            # TODO : here
            if school == 'hogwarts':
                logreg = LogisticRegression(path_to_beta='results/beta.json')
            else:
                logreg = LogisticRegression(path_to_beta='results/beta_%s.json' % school)



            prediction = logreg.predict(X_to_predict=np.array([[astronomy,
                                                               herbology,
                                                               ancient_runes]]))

            return str(prediction)
            #return jsonify ({'house':house, 'proba':proba})


        except ValueError:
            return "Please enter a number."



@app.route('/train')
def hello_world1():
    return 'Hello World 1!'




if __name__ == '__main__':
    app.run(debug = True)
