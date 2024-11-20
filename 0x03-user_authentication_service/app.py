#!/usr/bin/env python3
"""Define an app using flask."""
from flask import Flask, jsonify, Response, Request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """Get  a Json payload with a welcome message."""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Register users."""

    if request.method == "POST":
        the_email = request.form.get("email")
        email = the_email.strip()
        the_password = request.form.get("passowrd")
        password = the_password.strip()
        try:
            AUTH.register_user(email, password)
            message = jsonify({"email": email,
                              "message": "user created"})
            return message
        except Exception:
            return jsonify({"message": "email already registered"})
    else:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
