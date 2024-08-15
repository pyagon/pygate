"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from startup.database import db


class ApiService:
    api_collection = db.apis

    @staticmethod
    def create_api(data):
        if ApiService.api_collection.find_one({'name': data['name'], 'version': data['version']}):
            raise ValueError("API already exists for the requested name and version")
        ApiService.api_collection.insert_one(data)

# End of file
