import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()
    return True

def get_key(key_name):
    """Get environment variable value by key name"""
    return os.getenv(key_name)

def get_data_dir():
    """Get the data directory path from environment variables"""
    return get_key('DATA_DIR')

def get_api_key():
    """Get the API key from environment variables"""
    return get_key('API_KEY')
