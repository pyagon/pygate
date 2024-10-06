"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

class UserModel:

    def __init__ (self, username = None, email = None, password = None, role = None, groups = None, rate_limit = None, rate_limit_duration = None, throttle = None, throttle_duration = None):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.groups = groups
        self.rate_limit = rate_limit
        self.rate_limit_duration = rate_limit_duration
        self.throttle = throttle
        self.throttle_duration = throttle_duration

    def validate_api_creation(self):
        missing = []
        if not self.username: missing.append("username")
        if not self.email: missing.append("email")
        if not self.password: missing.append("password")
        if not self.role: missing.append("role")
        if not self.groups: missing.append("groups")
        if not self.rate_limit: missing.append("rate_limit")
        if not self.rate_limit_duration: missing.append("rate_limit_duration")
        if not self.throttle: missing.append("throttle")
        if not self.throttle_duration: missing.append("throttle_duration")
        if missing:
            raise ValueError(f"Missing required field(s): {', '.join(missing)}")
        
# End of file