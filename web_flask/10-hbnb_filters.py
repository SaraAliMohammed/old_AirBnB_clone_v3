#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def show_cities_by_states():
    """ Display a HTML page like 6-index.html,
    which was done during the project 0x01. AirBnB clone - Web static"""

    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
