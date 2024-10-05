#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HBNB_hello():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cdisplay(text):
    """display “C” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pydisplay(text='is cool'):
    """display Python followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Ndisplay(text='is cool'):
    """display The N is a number if only n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def Ntemplates(n):
    """display a HTML page only if N is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def NODDPREVEN(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        eve = 'even'
    else:
        eve = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           eve=eve)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
