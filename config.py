from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    PROXY_USERNAME = os.getenv('PROXY_USERNAME')
    PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')
    PROXY_HOSTNAME = os.getenv('PROXY_HOSTNAME')
    PROXY_PORT = os.getenv('PROXY_PORT')
    CHROME_USER_DATA_DIR = os.getenv('CHROME_USER_DATA_DIR')
    CHROME_PROFILE = os.getenv('CHROME_PROFILE')

    def __init__(self):
        print(f"Loading MongoDB URI: {self.MONGO_URI}")
    
    @property
    def PROXY_URL(self):
        return f"{self.PROXY_HOSTNAME}:{self.PROXY_PORT}"