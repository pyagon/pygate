"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Flask
from routes.users_routes import user_bp
from routes.api_routes import api_bp
from routes.endpoint_routes import endpoint_bp

pygate = Flask(__name__)
pygate.register_blueprint(user_bp, url_prefix='/users')
pygate.register_blueprint(api_bp, url_prefix='/api')
pygate.register_blueprint(endpoint_bp, url_prefix='/endpoint')

if __name__ == '__main__':
    try:
        pygate.run()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")

# End of file
