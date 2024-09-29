"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# External imports
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt


def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = get_jwt().get('role', None)
            if user_role not in allowed_roles:
                return jsonify({"message": "You do not have permission to access this resource"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# End of file
