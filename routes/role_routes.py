"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# External imports
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Internal imports
from services.role_service import RoleService
from utils.role_util import role_required

role_bp = Blueprint('role', __name__)


# Start role based endpoints

@role_bp.route('', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def create_role():
    """
    Create API *platform endpoint.
    Request:
    {
        "role_name": "<string>",
        "role_description": "<string>",
        "manage_users": "<boolean>",
        "manage_apis": "<boolean>",
        "manage_endpoints": "<boolean>",
        "manage_groups": "<boolean>",
        "manage_roles": "<boolean>"
    }
    Response:
    {
        "message": "Role created successfully"
    }
    """
    try:
        api_data = request.get_json()
        RoleService.create_role(api_data)
        return jsonify({'message': 'Role created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@role_bp.route('', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_roles():
    """
    Create API *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "roles": [
            {
                "role_name": "<string>",
                "role_description": "<string>",
                "manage_users": "<boolean>",
                "manage_apis": "<boolean>",
                "manage_endpoints": "<boolean>",
                "manage_groups": "<boolean>",
                "manage_roles": "<boolean>"
            }
        ]
    }
    """
    try:
        roles = RoleService.get_roles()
        return jsonify({roles}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@role_bp.route('<role_name>', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def get_role(role_name):
    """
    Create API *platform endpoint.
    Request:
    {
    }
    Response:
    {
        {
            "role_name": "<string>",
            "role_description": "<string>",
            "manage_users": "<boolean>",
            "manage_apis": "<boolean>",
            "manage_endpoints": "<boolean>",
            "manage_groups": "<boolean>",
            "manage_roles": "<boolean>"
        }
    }
    """
    try:
        role = RoleService.get_role(role_name)
        return jsonify({role}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End role based endpoints

# End of file
