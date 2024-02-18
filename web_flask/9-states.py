#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Display display a HTML page: (inside the tag BODY)
    H1 tag: 'States'
    UL tag: with the list of all State objects present
        in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>"""

    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
        H1 tag: 'State: '
        H3 tag: 'Cities:'
        UL tag: with the list of City objects linked to
            the State sorted by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: 'Not found!'
    """

    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
