"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# External imports
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Internal imports
from services.subscription_service import SubscriptionService
from utils.role_util import role_required

subscription_bp = Blueprint('subscription', __name__)

# Start role based endpoints
@subscription_bp.route('/subscribe', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def subscribe_api():
    """
    Subscribe to API *platform endpoint.
    Request:
    {
        "username": "<string>",
        "api_name": "<string>",
        "api_version": "<string>"
    }
    Response:
    {
        "message": "Successfully subscribed to the API"
    }
    """
    try:
        data = request.get_json()
        SubscriptionService.subscribe(data)
        return jsonify({'message': 'Successfully subscribed to the API'}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@subscription_bp.route('/unsubscribe', methods=['POST'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def unsubscribe_api():
    """
    Unsubscribe from API *platform endpoint.
    Request:
    {
        "username": "<string>",
        "api_name": "<string>",
        "api_version": "<string>"
    }
    Response:
    {
        "message": "Successfully unsubscribed from the API"
    }
    """
    try:
        data = request.get_json()
        SubscriptionService.unsubscribe(data)
        return jsonify({'message': 'Successfully unsubscribed from the API'}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    
@subscription_bp.route('/subscriptions/<user_id>', methods=['GET'])
@jwt_required()
@role_required(("admin", "dev", "platform"))
def subscriptions_for_user_by_id(user_id):
    """
    Get API Subscriptions for user by id *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "subscriptions": []
    }
    """
    try:
        subscriptions = SubscriptionService.get_user_subscriptions(user_id)
        return jsonify({'subscriptions': subscriptions}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# End role based endpoints
    
# Start active user endpoints

@subscription_bp.route('/subscriptions', methods=['GET'])
@jwt_required()
def subscriptions_for_current_user():
    """
    Get API Subscriptions for active user *platform endpoint.
    Request:
    {
    }
    Response:
    {
        "subscriptions": []
    }
    """
    try:
        username = get_jwt_identity()
        subscriptions = SubscriptionService.get_user_subscriptions(username)
        return jsonify({'subscriptions': subscriptions}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# End active user endpoint
    
# End of file
