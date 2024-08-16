"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from services.api_service import ApiService

api_bp = Blueprint('api', __name__)


@api_bp.route('', methods=['POST'])
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
        "message": "API created successfully",
        "api_id": "<string>"
    }
    """
    try:
        api_data = request.get_json()
        api = ApiService.create_api(api_data)
        return jsonify({'message': 'API created successfully', 'api_id': api['api_id']}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route('<api_id>', methods=['GET'])
def get_api_by_id(api_id):
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
        api = ApiService.get_api_by_id(api_id)
        return jsonify(api), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route('<api_name>/<api_version>', methods=['GET'])
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
