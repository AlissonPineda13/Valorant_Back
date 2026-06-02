from functools import wraps
from flask import request, jsonify
import os

def require_api_key(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        api_key = request.headers.get("X-API-KEY")

        if api_key != os.getenv("API_KEY"):
            return jsonify({
                "message": "Unauthorized"
            }), 401

        return f(*args, **kwargs)

    return decorated