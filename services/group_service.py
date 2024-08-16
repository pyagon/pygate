"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from utils.database import db


class GroupService:
    group_collection = db.group

    @staticmethod
    def create_group(data):
        if GroupService.group_collection.find_one({'group_name': data['group_name']}):
            raise ValueError("Group already exists")
        GroupService.group_collection.insert_one(data)

    @staticmethod
    def group_exists(data):
        if GroupService.group_collection.find_one({'group_name': data['group_name']}):
            return True
        return False

    @staticmethod
    def get_groups():
        return GroupService.group_collection.find_all()

# End of file
