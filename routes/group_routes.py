"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.group_service import GroupService
from utils.role_util import role_required

group_bp = Blueprint('group', __name__)


@group_bp.route('', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def create_group():
    """
    Create group *platform endpoint.
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


@group_bp.route('', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_groups():
    """
    Get groups *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "groups": [
            {
                "group_name": "<string>",
                "group_description": "<string>",
                "api_access": ["<string>"]
            }
        ]
    }
    """
    try:
        groups = GroupService.get_groups()
        return jsonify(groups), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@group_bp.route('<group_name>', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_group(group_name):
    """
    Get group *platform endpoint.
    Request:
    {
    }
    Response:
    {
        {
            "group_name": "<string>",
            "group_description": "<string>",
            "api_access": ["<string>"]
        }
        ]
    }
    """
    try:
        group = GroupService.get_group(group_name)
        return jsonify({group}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
