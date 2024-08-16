"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db


class RoleService:
    role_collection = db.roles

    @staticmethod
    def create_role(data):
        if RoleService.role_collection.find_one({'user_role': data['user_role']}):
            raise ValueError("Role already exists")
        RoleService.role_collection.insert_one(data)

    @staticmethod
    def role_exists(data):
        if RoleService.role_collection.find_one({'user_role': data['user_role']}):
            return True
        return False

    @staticmethod
    def get_roles():
        return RoleService.role_collection.find_all()

# End of file
