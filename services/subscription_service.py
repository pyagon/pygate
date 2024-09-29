"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# Internal imports
from services.api_service import ApiService
from utils.database import db
from utils.cache import cache_manager


class SubscriptionService:
    subscriptions_collection = db.subscriptions

    @staticmethod
    @cache_manager.get_cache().cached(timeout=300, query_string=True)
    def api_exists(api_name, api_version):
        """
        Check if an API exists.
        """
        return ApiService.api_collection.find_one({'api_name': api_name, 'api_version': api_version})

    @staticmethod
    @cache_manager.get_cache().cached(timeout=300, query_string=True)
    def get_user_subscriptions(username):
        """
        Get user subscriptions.
        """
        subscriptions = SubscriptionService.subscriptions_collection.find({'username': username})
        if not subscriptions:
            raise Exception('No subscriptions found for user')
        return subscriptions

    @staticmethod
    def subscribe(data):
        """
        Subscribe to an API.
        """
        username = data.get('username')
        api_name = data.get('api_name')
        api_version = data.get('api_version')
        if not SubscriptionService.api_exists(api_name, api_version):
            raise ValueError("API does not exist")
        if SubscriptionService.subscriptions_collection.find_one({'username': username})['apis'].contains(f"""{api_name}/{api_version}"""):
            raise ValueError("User is already subscribed to the API")
        SubscriptionService.subscriptions_collection.update_one(
            {'username': username},
            {'$push': {'apis': f"""{api_name}/{api_version}"""}})

    @staticmethod
    def unsubscribe(data):
        """
        Unsubscribe from an API.
        """
        username = data.get('username')
        api_name = data.get('api_name')
        api_version = data.get('api_version')
        if not SubscriptionService.api_exists(api_name, api_version):
            raise ValueError("API does not exist")
        if not SubscriptionService.subscriptions_collection.find_one({'username': username})['apis'].contains(
                f"""{api_name}/{api_version}"""):
            raise ValueError("User is already not subscribed to the API")
        SubscriptionService.subscriptions_collection.update_one(
            {'username': username},
            {'$pull': {'apis': f"""{api_name}/{api_version}"""}})

# End of file
