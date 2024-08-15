"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from services.group_service import GroupService

group_bp = Blueprint('group', __name__)


@group_bp.route('', methods=['POST'])
def create_group():
    """
    Create API *platform endpoint.
    Request:
    {
        "group_name": "<string>",
        "group_description": "<string>",
        "api_access": ["<string>"]
    }
    Response:
    {
        "message": "Group created successfully"
    }
    """
    try:
        api_data = request.get_json()
        GroupService.create_group(api_data)
        return jsonify({'message': 'Group created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
