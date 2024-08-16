"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from services.user_service import UserService

authorization_bp = Blueprint('authorization', __name__)


@authorization_bp.route('/authorization', methods=['POST'])
def authorization():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({"msg": "Missing username or password"}), 400
        UserService.check_password(username, password)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400