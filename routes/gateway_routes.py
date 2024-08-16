"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

gateway_bp = Blueprint('gateway', __name__)


@gateway_bp.route('/', defaults={'path': ''})
@gateway_bp.route('/<path:path>')
@jwt_required()
def catch_all(path):
    # This is the API Gateway.. TODO: Build the gateway.
    return f"Requested path: {path}"

# End of file
