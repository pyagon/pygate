#  The contents of this file are property of pygate.org
#  Review the Apache License 2.0 for valid uses
#  See https://github.com/pygate-dev/pygate for more information

class Config:

    def __init__(self):
        self.MONGODB_URI = 'mongodb://localhost:27017/pygate'

    def get_mongodb_uri(self):
        return self.MONGODB_URI


# Create an instance of Config
config = Config()

# End of file
