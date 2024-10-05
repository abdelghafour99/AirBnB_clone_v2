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
def Ndisplay(n):
    """display The N is a number if only n is an integer"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
