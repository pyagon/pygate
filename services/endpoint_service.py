"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# Internal imports
from utils.database import db
from utils.cache import cache_manager

class EndpointService:
    api_collection = db.apis
    endpoint_collection = db.endpoints

    @staticmethod
    def create_endpoint(data):
        """
        Onboard an endpoint to the platform.
        """
        api = EndpointService.api_collection.find_one({'name': data.get('api_name'), 'version': data.get('api_version')})
        if api:
            if EndpointService.endpoint_collection.find_one(
                    {'endpoint_method': data.get('endpoint_method'), 'endpoint_uri': data.get('endpoint_uri'),
                     'api_id': api.get('api_id')}):
                raise ValueError("Endpoint already exists for the requested API version")
            else:
                EndpointService.endpoint_collection.insert_one(data)
        else:
            raise ValueError("API does not exist")

    @staticmethod
    @cache_manager.get_cache().cached(timeout=300, query_string=True)
    def get_endpoints_by_name_version(api_name, api_version):
        """
        Get endpoints by API name and version.
        """
        api = EndpointService.api_collection.find_one({'api_name': api_name, 'api_version': api_version})
        if api:
            endpoints = EndpointService.endpoint_collection.find({'api_id': api['api_id']})
            if endpoints:
                endpoints = [{'endpoint_method': endpoint.get('endpoint_method'), 'endpoint_uri': endpoint.get('endpoint_uri')}
                             for endpoint in endpoints]
            return {'api_name': api.get('name'), 'api_version': api.get('version'), 'endpoints': endpoints}
        else:
            raise ValueError("API does not exist")

# End of file
