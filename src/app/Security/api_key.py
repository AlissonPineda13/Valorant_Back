from functools import wraps
from flask import current_app, request, jsonify
import os

def require_api_key(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        api_key = request.headers.get("X-API-KEY")

        if api_key != current_app.config["API_KEY"]:
            return jsonify({
                "message": "Unauthorized"
            }), 401

        return f(*args, **kwargs)

    return decorated