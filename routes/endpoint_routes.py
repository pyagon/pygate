"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from flask import Blueprint, request, jsonify
from services.endpoint_service import EndpointService

endpoint_bp = Blueprint('endpoint', __name__)

endpoint_bp.route('', methods=['POST'])


@endpoint_bp.route('', methods=['POST'])
def create_endpoint(api_id):
    try:
        endpoint_data = request.get_json()
        EndpointService.create_endpoint(endpoint_data)
        return jsonify({'message': 'Endpoint created successfully'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End of file
