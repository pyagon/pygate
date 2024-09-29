"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db
from pygate import cache


class RoleService:
    role_collection = db.roles

    @staticmethod
    def create_role(data):
        """
        Onboard a role to the platform.
        """
        if RoleService.role_collection.find_one({'role_name': data.get('role')}):
            raise ValueError("Role already exists")
        RoleService.role_collection.insert_one(data)

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def role_exists(data):
        """
        Check if a role exists.
        """
        if RoleService.role_collection.find_one({'role_name': data.get('role')}):
            return True
        return False

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def get_roles():
        """
        Get all roles.
        """
        return RoleService.role_collection.find_all()

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def get_role(role_name):
        """
        Get a role by name.
        """
        role = RoleService.role_collection.find_one({'group_name': role_name})
        if not role:
            raise ValueError("Role not found")
        return role

# End of file
