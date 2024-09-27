"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from flask_caching import Cache
from dotenv import load_dotenv

from routes.authorization_routes import authorization_bp
from routes.group_routes import group_bp
from routes.role_routes import role_bp
from routes.subscription_routes import subscription_bp
from routes.user_routes import user_bp
from routes.api_routes import api_bp
from routes.endpoint_routes import endpoint_bp
from routes.gateway_routes import gateway_bp

import logging
import os

pygate = Flask(__name__)
#cache = Cache(pygate, config={'CACHE_TYPE': 'redis'})
CORS(pygate)
logging.basicConfig(level=logging.INFO)

load_dotenv()

pygate.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
pygate.config['MONGODB_URI'] = os.getenv("MONGO_DB_URI")

jwt = JWTManager(pygate)

pygate.register_blueprint(gateway_bp, url_prefix='/api')
pygate.register_blueprint(authorization_bp, url_prefix='/platform')
pygate.register_blueprint(user_bp, url_prefix='/platform/user')
pygate.register_blueprint(api_bp, url_prefix='/platform/api')
pygate.register_blueprint(endpoint_bp, url_prefix='/platform/endpoint')
pygate.register_blueprint(group_bp, url_prefix='/platform/group')
pygate.register_blueprint(role_bp, url_prefix='/platform/role')
pygate.register_blueprint(subscription_bp, url_prefix='/platform/subscription')

http_server = WSGIServer(('', 5000), pygate)
logging.info("Pygate HTTP server started on port 5000")
http_server.serve_forever()

# End of file
