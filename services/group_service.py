"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db
from pygate import cache


class GroupService:
    group_collection = db.group

    @staticmethod
    def create_group(data):
        """
        Onboard a group to the platform.
        """
        if GroupService.group_collection.find_one({'group_name': data.get('group_name')}):
            raise ValueError("Group already exists")
        GroupService.group_collection.insert_one(data)

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def group_exists(data):
        """
        Check if a group exists.
        """
        if GroupService.group_collection.find_one({'group_name': data.get('group_name')}):
            return True
        return False

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def get_groups():
        """
        Get all groups.
        """
        return GroupService.group_collection.find_all()

    @staticmethod
    @cache.cached(timeout=300, query_string=True)
    def get_group(group_name):
        """
        Get a group by name.
        """
        group = GroupService.group_collection.find_one({'group_name': group_name})
        if not group:
            raise ValueError("Group not found")
        return group

# End of file
