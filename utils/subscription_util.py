"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# External imports
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

# Internal imports
from services.subscription_service import SubscriptionService

def subscription_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            username = get_jwt_identity()
            subscriptions = set(SubscriptionService.subscriptions_collection.find({'username': username}))
            path = kwargs.get('path', '')
            if path not in subscriptions:
                return jsonify({"message": "You are not subscribed to this resources"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# End of file
