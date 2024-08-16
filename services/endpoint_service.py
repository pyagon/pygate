"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db


class EndpointService:
    api_collection = db.apis
    endpoint_collection = db.endpoints

    @staticmethod
    def create_endpoint(data):
        api = EndpointService.api_collection.find_one({'name': data['api_name'], 'version': data['api_version']})
        if api:
            if EndpointService.endpoint_collection.find_one({'endpoint_method': data['endpoint_method'], 'endpoint_uri': data['endpoint_uri'], 'api_id': api['api_id']}):
                raise ValueError("Endpoint already exists for the requested API version")
            else:
                EndpointService.endpoint_collection.insert_one(data)
        else:
            raise ValueError("API does not exist")

    @staticmethod
    def get_endpoints_by_id(api_id):
        api = EndpointService.api_collection.find_one({'api_id': api_id})
        if api:
            endpoints = EndpointService.endpoint_collection.find({'api_id': api_id})
            if endpoints:
                endpoints = [{'endpoint_method': endpoint['endpoint_method'], 'endpoint_uri': endpoint['endpoint_uri']} for endpoint in endpoints]
            return {'api_name': api['name'], 'api_version': api['version'], 'endpoints': endpoints}
        else:
            raise ValueError("API does not exist")

    @staticmethod
    def get_endpoints_by_name_version(api_name, api_version):
        api = EndpointService.api_collection.find_one({'api_name': api_name, 'api_version': api_version})
        if api:
            endpoints = EndpointService.endpoint_collection.find({'api_id': api['api_id']})
            if endpoints:
                endpoints = [{'endpoint_method': endpoint['endpoint_method'], 'endpoint_uri': endpoint['endpoint_uri']} for endpoint in endpoints]
            return {'api_name': api['name'], 'api_version': api['version'], 'endpoints': endpoints}
        else:
            raise ValueError("API does not exist")

# End of file
