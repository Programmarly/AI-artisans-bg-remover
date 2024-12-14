from dotenv import load_dotenv
import os

class Config:
    CLOUD_NAME = os.getenv("CLOUD_NAME")
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    PROCESSED_IMAGES_DIR = os.getenv("PROCESSED_IMAGES_DIR")
    DEFAULT_LIMITS = os.getenv("DEFAULT_LIMITS")
