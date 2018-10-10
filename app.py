from flask import Flask

"""
- https://www.wintellect.com/creating-machine-learning-web-api-flask/
- https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
"""


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/train')
def hello_world1():
    return 'Hello World 1!'


@app.route('/predict')
def hello_world2():
    return 'Hello World 2!'




if __name__ == '__main__':
    app.run()
