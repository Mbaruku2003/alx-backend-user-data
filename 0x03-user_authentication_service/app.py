#!/usr/bin/env python3
"""Define an app using flask."""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=["Get"])
def welcome():
    """Get  a Json payload with a welcome message."""

    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    """POSTS uSERS."""

    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
