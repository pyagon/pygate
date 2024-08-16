"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db


class ApiService:
    api_collection = db.apis

    @staticmethod
    def create_api(data):
        if ApiService.api_collection.find_one({'api_name': data['api_name'], 'api_version': data['api_version']}):
            raise ValueError("API already exists for the requested name and version")
        api = ApiService.api_collection.insert_one(data)
        return api

    @staticmethod
    def get_api_by_id(api_id):
        api = ApiService.api_collection.find_one({'api_id': api_id})
        if not api:
            raise ValueError("API already exists for the requested name and version")
        api['path'] = f"/{api['api_name']}/{api['api_version']}"
        return api

    @staticmethod
    def get_api_by_name_version(api_name, api_version):
        api = ApiService.api_collection.find_one({'api_name': api_name, 'api_version': api_version})
        if not api:
            raise ValueError("API already exists for the requested name and version")
        api['path'] = f"/{api['api_name']}/{api['api_version']}"
        return api


# End of file
