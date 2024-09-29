"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# Internal imports
from utils.database import db
from utils.cache import cache_manager


class ApiService:
    api_collection = db.apis

    @staticmethod
    def create_api(data):
        """
        Onboard an API to the platform.
        """
        if ApiService.api_collection.find_one({'api_name': data.get('api_name'), 'api_version': data.get('api_version')}):
            raise ValueError("API already exists for the requested name and version")
        ApiService.api_collection.insert_one(data)

    @staticmethod
    @cache_manager.get_cache().cached(timeout=300, query_string=True)
    def get_api_by_name_version(api_name, api_version):
        """
        Get an API by name and version.
        """
        api = ApiService.api_collection.find_one({'api_name': api_name, 'api_version': api_version})
        if not api:
            raise ValueError("API does not exists for the requested name and version")
        api['path'] = f"/{api.get('api_name')}/{api.get('api_version')}"
        return api


# End of file
