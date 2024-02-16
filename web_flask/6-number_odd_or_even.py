#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ hello home page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB page """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Display 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space  """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """ Display 'Python ', followed by the value of the text variable
    (replace underscore _ symbols with a space ) """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    """ Display 'n is a number' only if n is an integer """
    return "{:d} is a number".format(num)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ display a HTML page only if n is an integer:
        H1 tag: 'Number: n is even|odd' inside the tag BODY """
    n_type = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, type=n_type)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
