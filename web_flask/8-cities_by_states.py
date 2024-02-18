#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def show_cities_by_states():
    """ Display a HTML page: (inside the tag BODY)
        H1 tag: 'States'
        UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
        LI tag: description of one State:
            <state.id>: <B><state.name></B>
        City objects linked to the State sorted by name (A->Z)
            LI tag: description of one City:
                <city.id>: <B><city.name></B>"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
