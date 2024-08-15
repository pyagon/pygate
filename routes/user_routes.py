"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint('users', __name__)


@user_bp.route('', methods=['POST'])
def create_user():
    """
    Create user *platform endpoint.
    Request:
    {
        "username": "<string>",
        "email": "<string>",
        "password": "<string>"
        "user_role": "<string>"
        "user_groups": ["<string>"]
    }
    Response:
    {
        "message": "User created successfully",
        "user_details" {
            "user_id": "<string>",
            "email": "<string>"
        }
    }
    """
    try:
        user_data = request.get_json()
        new_user = UserService.create_user(user_data)
        return jsonify({'message': 'User created successfully', 'user_details': new_user}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update user *platform endpoint.
    Request:
    {
        "email": "<string>",
        "user_role": "<string>",
        "user_groups": ["<string>"]
    }
    Response:
    {
        "message": "User updated successfully",
        "user_details" {
            "user_id": "<string>",
            "email": "<string>"
        }
    }
    """
    try:
        update_data = request.get_json()
        updated_user = UserService.update_user(user_id, update_data)
        return jsonify({'message': 'User updated successfully', 'user': updated_user}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route('/<user_id>/update-password', methods=['PUT'])
def update_user_password(user_id):
    """
    Update user *platform endpoint.
    Request:
    {
        "current_password": "<string>",
        "new_password": "<string>"
    }
    Response:
    {
        "message": "Password updated successfully"
    }
    """
    try:
        data = request.get_json()
        current_password = data.get('current_password')
        new_password = data.get('new_password')
        if not current_password:
            return jsonify({"error": "Current password is required"}), 400
        if not new_password:
            return jsonify({"error": "New password is required"}), 400
        UserService.update_password(user_id, current_password, new_password)
        return jsonify({'message': 'Password updated successfully'}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
