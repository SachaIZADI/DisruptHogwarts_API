from flask import Flask, jsonify, request
import numpy as np
import json
from model.logistic_regression import LogisticRegression
from model.preprocessing import Scaling
import model.logreg_train

"""
- https://www.wintellect.com/creating-machine-learning-web-api-flask/
- https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
- https://github.com/Wintellect/DataScienceExamples/blob/master/Regression/SimpleLinearRegressionAPI.py
"""


app = Flask(__name__)



# Train the model on the base dataset
@app.route('/train')
def train():
    if request.method == 'GET':
        features, beta = model.logreg_train.train()
        features = list(features)
        for b in beta :
            beta[b] = list(beta[b])
        return jsonify({'features':features, 'beta':beta})



# Make a prediction: argmax P(y|X=x)
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        try:
            try:
                # Data is sent via a .py script like in tests/test_api.py
                data = json.loads(request.json)
                school = data['school']
                astronomy = float(data['astronomy']) # -1000 < astronomy < 1000
                herbology = float(data['herbology']) # -10 < herbology < 10
                ancient_runes = float(data['ancient_runes']) # 250 < ancient_runes < 750
            except:
                # Data is sent via an url (e.g. in Chrome)
                # http://127.0.0.1:5000/predict?school=hogwarts&astronomy=-800&herbology=-2&ancient_runes=300
                data = request.args
                school = data.get('school')
                astronomy = float(data.get('astronomy'))
                herbology = float(data.get('herbology'))
                ancient_runes = float(data.get('ancient_runes'))

            X = np.array([[astronomy, herbology, ancient_runes]])

            if school == 'hogwarts':
                logreg = LogisticRegression(path_to_beta='results/beta.json')
                sc = Scaling(X, path_to_scaling='results/scaling.json')
            else:
                logreg = LogisticRegression(path_to_beta='results/beta_%s.json' % school)
                sc = Scaling(X, path_to_scaling='results/scaling_%s.json' % school)

            sc.transform()
            prediction = logreg.predict(X_to_predict=sc.X)

            return jsonify({'house':prediction[0][0],'probas':prediction[1][0]})

        except ValueError:
            return "Please enter values in the correct format: {\"school\":str, \"astronomy\":-1000<float<1000, \"herbology\":-10<float<10, \"ancient_runes\":250<float<750}."


@app.route('/transfer')
def transfer():
    return(True)




if __name__ == '__main__':
    app.run(debug = True)
