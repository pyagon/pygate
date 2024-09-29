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
import sys
import subprocess
import signal

load_dotenv()

PID_FILE = "pygate.pid"

pygate = Flask(__name__)
CORS(pygate)
logging.basicConfig(level=logging.INFO)

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


def start():
    if os.path.exists(PID_FILE):
        print("Pygate is already running!")
        sys.exit(0)

    process = subprocess.Popen([sys.executable, __file__, "run"], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               preexec_fn=os.setpgrp if os.name != "nt" else None)

    with open(PID_FILE, "w") as f:
        f.write(str(process.pid))
    print(f"Pygate started with PID {process.pid}.")

def stop():
    if not os.path.exists(PID_FILE):
        print("No running instance found.")
        return

    with open(PID_FILE, "r") as f:
        pid = int(f.read())
    
    try:
        if os.name == "nt":
            subprocess.call(["taskkill", "/F", "/PID", str(pid)])
        else:
            os.killpg(pid, signal.SIGTERM)
        print(f"Pygate with PID {pid} has been stopped.")
    except ProcessLookupError:
        print("Process already terminated.")
    
    os.remove(PID_FILE)

def run():
    http_server = WSGIServer(('', 5000), pygate)
    logging.info("Pygate HTTP server started on port 5000")
    http_server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run()
    elif len(sys.argv) > 1 and sys.argv[1] == "stop":
        stop()
    else:
        start()

# End of file
