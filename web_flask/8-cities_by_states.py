#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask, render_template

=======
"""Importing Flask to run the web app"""
from flask import Flask, render_template
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
from models import storage
from models.state import State


app = Flask(__name__)
<<<<<<< HEAD
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    '''The cities_by_states page.'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
