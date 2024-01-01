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


@app.route('/states_list')
def states_list():
    '''The states_list page.'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
