#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display a HTML page like 8-index.html,
    which was done during the project 0x01. AirBnB clone - Web static"""

    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
