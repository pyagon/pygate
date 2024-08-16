"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from pymongo import MongoClient, IndexModel, ASCENDING

from utils import password_util
from utils.config import Config

pygate_config = Config()


class Database:
    def __init__(self):
        self.client = MongoClient(pygate_config.get_mongodb_uri(), serverSelectionTimeoutMS=5000)
        self.db = self.client.get_database()
        self.initialize_collections()
        self.create_indexes()

    def initialize_collections(self):
        collections = ['users', 'apis', 'endpoints', 'groups', 'roles']
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
            IndexModel([("username", ASCENDING)], unique=True),
            IndexModel([("email", ASCENDING)], unique=True)
        ])

        self.db.groups.create_indexes([
            IndexModel([("group_name", ASCENDING)], unique=True)
        ])

        self.db.roles.create_indexes([
            IndexModel([("user_role", ASCENDING)], unique=True)
        ])

        self.db.subscriptions.create_indexes([
            IndexModel([("username", ASCENDING)], unique=True)
        ])

        if not self.db.users.find_one({"username": "admin"}):
            self.db.users.insert_one({
                "username": "admin",
                "email": "admin@pygate.org",
                "password": password_util.hash_password("password123"),
                "role": "admin",
                "groups": ["ALL"]
            })


database = Database()

database.initialize_collections()
database.create_indexes()

db = database.db

# End of file
