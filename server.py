
from flask import Flask, request, jsonify
import time
import secrets

app = Flask(__name__)

# Demo client credentials
CLIENT_ID = "my_client"
CLIENT_SECRET = "my_secret"

# Store tokens and their expiry times
tokens = {}


@app.route("/token", methods=["POST"])
def get_token():

    client_id = request.form.get("client_id")
    client_secret = request.form.get("client_secret")

    # Check client credentials
    if client_id != CLIENT_ID or client_secret != CLIENT_SECRET:
        return jsonify({"error": "Invalid client"}), 401

    # Create a new token
    access_token = secrets.token_urlsafe(16)

    # Token expires after 30 seconds
    expiry_time = time.time() + 30

    tokens[access_token] = expiry_time

    return jsonify({
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 30
    })


@app.route("/data", methods=["GET"])
def get_data():

    # Get token from Authorization header
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"error": "Token missing"}), 401

    # Remove the word Bearer
    token = auth_header.replace("Bearer ", "")

    # Check whether token exists
    if token not in tokens:
        return jsonify({"error": "Invalid token"}), 401

    # Check whether token expired
    if time.time() > tokens[token]:
        return jsonify({"error": "Token expired"}), 401

    return jsonify({
        "message": "You accessed the protected data!",
        "data": "This is secret API data"
    })


if __name__ == "__main__":
    app.run(port=8000, debug=True)
