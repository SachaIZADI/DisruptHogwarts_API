from flask import Flask
from model.logistic_regression import LogisticRegression
import request
import numpy as np

"""
- https://www.wintellect.com/creating-machine-learning-web-api-flask/
- https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
"""


app = Flask(__name__)


@app.route('/predict')
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()

            school = data['school']
            astronomy = float(data['astronomy'])
            herbology = float(data['herbology'])
            ancient_runes = float(data['ancient_runes'])

            # TODO : here
            if school == 'hogwarts':
                logreg = LogisticRegression(path_to_beta='model/results/beta.json')
            else:
                logreg = LogisticRegression(path_to_beta='model/results/beta_%s.json' % school)

            prediction = logreg.predict(X_to_predict=np.array([[astronomy],
                                                               [herbology],
                                                               [ancient_runes]]))

            
            # return jsonify ({'house':house, 'proba':proba})











            lin_reg = joblib.load("./linear_regression_model.pkl")
        except ValueError:
            return jsonify("Please enter a number.")

        return jsonify(lin_reg.predict(years_of_experience).tolist())


@app.route('/train')
def hello_world1():
    return 'Hello World 1!'




if __name__ == '__main__':
    app.run()
