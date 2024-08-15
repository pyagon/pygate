"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from startup.database import db


class EndpointService:
    api_collection = db.apis
    endpoint_collection = db.endpoints

    @staticmethod
    def create_endpoint(data):
        if EndpointService.api_collection.find_one({'name': data['api_name'], 'version': data['api_version']}):
            if EndpointService.endpoint_collection.find_one({'uri': data['endpoint_uri'], 'api_name': data['api_name'], 'api_version': data['api_version']}):
                raise ValueError("Endpoint already exists for the requested API version")
            else:
                EndpointService.endpoint_collection.insert_one(data)
        else:
            raise ValueError("API does not exist")

# End of file
