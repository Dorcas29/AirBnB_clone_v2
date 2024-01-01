#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
