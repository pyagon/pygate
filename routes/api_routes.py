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
    try:
        api_data = request.get_json()
        ApiService.create_api(api_data)
        return jsonify({'message': 'API created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
