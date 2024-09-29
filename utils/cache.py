"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

# External imports
from flask_caching import Cache
from dotenv import load_dotenv
import os

load_dotenv()

class CacheManager:
    def __init__(self, app=None):
        self.cache = Cache(app, config={
            'CACHE_TYPE': 'redis',
            'CACHE_REDIS_HOST': os.getenv("REDIS_HOST"),
            'CACHE_REDIS_PORT': os.getenv("REDIS_PORT"),
            'CACHE_REDIS_DB': os.getenv("REDIS_DB"),
            'CACHE_DEFAULT_TIMEOUT': 300
        })

    def get_cache(self):
        return self.cache

cache_manager = CacheManager()

# End of file
