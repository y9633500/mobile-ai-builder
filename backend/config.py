# Configuration for API Keys and Environment Settings

import os

class Config:
    # API Keys
    API_KEY_1 = os.getenv('API_KEY_1')
    API_KEY_2 = os.getenv('API_KEY_2')

    # Database Settings
    DB_URL = os.getenv('DB_URL')

    # Other configuration settings
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
