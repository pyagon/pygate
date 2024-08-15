"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Flask

from routes.group_routes import group_bp
from routes.role_routes import role_bp
from routes.user_routes import user_bp
from routes.api_routes import api_bp
from routes.endpoint_routes import endpoint_bp
from routes.gateway_routes import gateway_bp

pygate = Flask(__name__)
pygate.register_blueprint(user_bp, url_prefix='/user')
pygate.register_blueprint(api_bp, url_prefix='/api')
pygate.register_blueprint(endpoint_bp, url_prefix='/endpoint')
pygate.register_blueprint(group_bp, url_prefix='/group')
pygate.register_blueprint(role_bp, url_prefix='/role')
pygate.register_blueprint(gateway_bp)

if __name__ == '__main__':
    try:
        pygate.run()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")

# End of file
