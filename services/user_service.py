"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

from services.group_service import GroupService
from services.role_service import RoleService

from utils import password_util
from utils.database import db


class UserService:
    user_collection = db.users
    @staticmethod
    def find_user(user_data):
        return UserService.user_collection.find_one({'_id': user_data['user_id']})

    @staticmethod
    def get_user_by_username(username):
        user = UserService.user_collection.find_one({'username': username})
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_user_by_email(email):
        user = UserService.user_collection.find_one({'email': email})
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def create_user(user_data):
        if UserService.find_user({'username': user_data['username']}):
            raise ValueError(f"User {user_data['username']} already exists")
        if UserService.find_user({'email': user_data['email']}):
            raise ValueError(f"Email {user_data['email']} connected to an existing user")
        if not RoleService.role_exists({'user_role': user_data['user_role']}):
            raise ValueError(f"Role {user_data['user_role']} does not exist")
        for group in user_data['user_groups']:
            if not GroupService.group_exists({'group_name': group}):
                raise ValueError(f"Group {group} does not exist")
        hashed_password = password_util.hash_password(user_data['password'])
        if not password_util.verify_password(user_data['password'], hashed_password):
            raise ValueError("Unable to hash password")
        user_data['password'] = hashed_password
        UserService.user_collection.insert_one(user_data)
        user_data['password'] = None
        return user_data

    @staticmethod
    def update_user(user_id, update_data):
        existing_user = UserService.find_user({'user_id': user_id})
        if not existing_user:
            raise ValueError("User not found")
        UserService.user_collection.updatep_one({'_id': user_id}, {'$set': update_data})

    @staticmethod
    def update_password(user_id, current_password, new_password):
        user = UserService.find_user({'user_id': user_id})
        if not user:
            raise ValueError("User not found")
        if not password_util.verify_password(current_password, user['password']):
            raise ValueError("Current password is incorrect")
        hashed_password = password_util.hash_password(new_password)
        UserService.user_collection.update_one({'_id': user_id}, {'$set': {'password': hashed_password}})

# End of file
