"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""
from random import random

# Start of file

from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from routes.group_routes import group_bp
from routes.role_routes import role_bp
from routes.subscription_routes import subscription_bp
from routes.user_routes import user_bp
from routes.api_routes import api_bp
from routes.endpoint_routes import endpoint_bp
from routes.gateway_routes import gateway_bp

import secrets

pygate = Flask(__name__)

pygate.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
jwt = JWTManager(pygate)
pygate.register_blueprint(gateway_bp, url_prefix='/api')
pygate.register_blueprint(user_bp, url_prefix='/platform/user')
pygate.register_blueprint(api_bp, url_prefix='/platform/api')
pygate.register_blueprint(endpoint_bp, url_prefix='/platform/endpoint')
pygate.register_blueprint(group_bp, url_prefix='/platform/group')
pygate.register_blueprint(role_bp, url_prefix='/platform/role')
pygate.register_blueprint(subscription_bp, url_prefix='/platform/subscription')

if __name__ == '__main__':
    try:
        pygate.run()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")

# End of file
