#!/usr/bin/env python3
"""Define an app using flask."""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["Get"])
def welcome():
    """Get  a Json payload with a welcome message."""

    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
