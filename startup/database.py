"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

import sys
from pymongo import MongoClient, IndexModel, ASCENDING
from startup.config import Config

pygate_config = Config()


class Database:
    def __init__(self):
        self.client = MongoClient(pygate_config.get_mongodb_uri(), serverSelectionTimeoutMS=5000)
        self.db = self.client.get_database()
        self.initialize_collections()
        self.create_indexes()

    def initialize_collections(self):
        collections = ['users', 'apis', 'endpoints', 'rate_limits', 'throttle_limits']
        for collection in collections:
            if collection not in self.db.list_collection_names():
                self.db.create_collection(collection)
                print(f'Created collection: {collection}')

    def create_indexes(self):
        self.db.apis.create_indexes([
            IndexModel([("api_id", ASCENDING)], unique=True),
            IndexModel([("name", ASCENDING), ("version", ASCENDING)])
        ])

        self.db.endpoints.create_indexes([
            IndexModel([("api_id", ASCENDING)], unique=True),
            IndexModel([("api_name", ASCENDING), ("version", ASCENDING)]),
            IndexModel([("api_name", ASCENDING), ("version", ASCENDING), ("path", ASCENDING)], unique=True)
        ])

        self.db.users.create_indexes([
            IndexModel([("user_id", ASCENDING)], unique=True),
            IndexModel([("email", ASCENDING)], unique=True)
        ])


database = Database()

database.initialize_collections()
database.create_indexes()

db = database.db

# End of file
