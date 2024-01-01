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


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    '''The states page.'''
    states = None
    state = None
    all_states = list(storage.all(State).values())
    case = 404
    if id is not None:
        res = list(filter(lambda x: x.id == id, all_states))
        if len(res) > 0:
            state = res[0]
            state.cities.sort(key=lambda x: x.name)
            case = 2
    else:
        states = all_states
        for state in states:
            state.cities.sort(key=lambda x: x.name)
        states.sort(key=lambda x: x.name)
        case = 1
    ctxt = {
        'states': states,
        'state': state,
        'case': case
    }
    return render_template('9-states.html', **ctxt)


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


@app.route('/states', strict_slashes=False)
def state():
    """Displays a html page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays a html page with citys of that state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
