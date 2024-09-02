"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.endpoint_service import EndpointService
from utils.role_util import role_required

endpoint_bp = Blueprint('endpoint', __name__)


@endpoint_bp.route('', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def create_endpoint():
    """
    Create endpoint *platform endpoint.
    Request:
    {
        "api_name": "<string>",
        "api_version": "<string>",
        "endpoint_method": "<string>",
        "endpoint_uri": "<string>"
    }
    Response:
    {
        "message": "Endpoint created successfully"
    }
    """
    try:
        endpoint_data = request.get_json()
        EndpointService.create_endpoint(endpoint_data)
        return jsonify({'message': 'Endpoint created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@endpoint_bp.route('/api/<api_name>/<api_version>', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_endpoints_by_name_version(api_id):
    """
    Get endpoints *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "api_name": "<string>",
        "api_version": "<string>",
        "endpoints": [
            {
                "endpoint_method": "<string>",
                "endpoint_uri": "<string>"
            }
        ]
    }
    """
    try:
        endpoints = EndpointService.get_endpoints_by_name_version(api_id)
        return jsonify({endpoints}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
