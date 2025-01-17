#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask, render_template


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


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''The python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''The number page.'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''The number_template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
