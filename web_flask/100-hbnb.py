#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask, render_template, Markup

from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    all_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    places.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    ctxt = {
        'states': all_states,
        'amenities': amenities,
        'places': places
    }
    return render_template('100-hbnb.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 172675bbd6c5a79817531dc5a14d4b9af11b3361
