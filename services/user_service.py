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
        return UserService.user_collection.find_one({'username': user_data.get('username')})

    @staticmethod
    def find_user_email(user_data):
        return UserService.user_collection.find_one({'email': user_data.get('email')})

    @staticmethod
    def get_user_by_username(username):
        user = UserService.user_collection.find_one({'username': username})
        if not user:
            raise ValueError("User not found")
        del user['_id']
        del user['password']
        return user

    @staticmethod
    def get_user_by_email(email):
        user = UserService.user_collection.find_one({'email': email})
        if not user:
            raise ValueError("User not found")
        del user['_id']
        del user['password']
        return user

    @staticmethod
    def create_user(user_data):
        if UserService.find_user({'username': user_data.get('username')}):
            raise ValueError(f"User {user_data.get('username')} already exists")
        if UserService.find_user_email({'email': user_data.get('email')}):
            raise ValueError(f"Email {user_data.get('email')} connected to an existing user")
        if not RoleService.role_exists({'role': user_data.get('role')}):
            raise ValueError(f"Role {user_data.get('role')} does not exist")
        for group in user_data.get('groups'):
            if not GroupService.group_exists({'group_name': group}):
                raise ValueError(f"Group {group} does not exist")
        hashed_password = password_util.hash_password(user_data.get('password'))
        if not password_util.verify_password(user_data.get('password'), hashed_password):
            raise ValueError("Unable to hash password")
        user_data['password'] = hashed_password
        UserService.user_collection.insert_one(user_data)
        del user_data['password']
        del user_data['_id']
        return user_data

    @staticmethod
    def update_user(username, update_data):
        existing_user = UserService.find_user({'username': username})
        if not existing_user:
            raise ValueError("User not found")
        UserService.user_collection.updatep_one({'username': username}, {'$set': update_data})

    @staticmethod
    def update_password(username, current_password, new_password):
        user = UserService.find_user({'username': username})
        if not user:
            raise ValueError("User not found")
        if not password_util.verify_password(current_password, user['password']):
            raise ValueError("Current password is incorrect")
        hashed_password = password_util.hash_password(new_password)
        UserService.user_collection.update_one({'username': username}, {'$set': {'password': hashed_password}})

    @staticmethod
    def check_password(username, password):
        user = UserService.find_user({'username': username})
        if not user:
            raise ValueError("User not found")
        if not password_util.verify_password(password, user['password']):
            raise ValueError("Incorrect username and password combination")

    @staticmethod
    def check_password_return_user(username, password):
        user = UserService.user_collection.find_one({'username': username})
        if not user:
            raise ValueError("User not found")
        if not password_util.verify_password(password, user.get('password')):
            raise ValueError("Incorrect username and password combination")
        return user

# End of file
