"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from services.api_service import ApiService
from utils.role_util import role_required

api_bp = Blueprint('api', __name__)


@api_bp.route('', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def create_api():
    """
    Create API *platform endpoint.
    Request:
    {
        "api_name": "<string>",
        "api_version": "<string>",
        "api_description": "<string>"
    }
    Response:
    {
        "message": "API created successfully"
    }
    """
    try:
        api_data = request.get_json()
        ApiService.create_api(api_data)
        return jsonify({'message': 'API created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route('<api_name>/<api_version>', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_api_by_name_version(api_name, api_version):
    """
    Get API *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "api_name": "<string>",
        "api_version": "<string>",
        "api_description": "<string>",
        "api_path": "<string>"
    }
    """
    try:
        api = ApiService.get_api_by_name_version(api_name, api_version)
        return jsonify(api), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
