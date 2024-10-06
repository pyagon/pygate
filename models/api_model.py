"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

class ApiModel:

    def __init__ (self, api_name = None, api_version = None, api_description = None, api_servers = None):
        self.api_name = api_name
        self.api_version = api_version
        self.api_description = api_description
        self.api_servers = api_servers

    def validate_api_creation(self):
        missing = []
        if not self.api_name: missing.append("api_name")
        if not self.api_version: missing.append("api_version")
        if not self.api_description: missing.append("api_description")
        if not self.api_servers: missing.append("api_servers")
        if missing:
            raise ValueError(f"Missing required field(s): {', '.join(missing)}")
        
# End of file