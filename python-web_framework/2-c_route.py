# /usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    msg = "C {}".format(text.replace("_", " "))
    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
