import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings class."""
    
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./calendar_assistant.db")
    
    # Google Calendar settings
    GOOGLE_CALENDAR_CREDENTIALS_PATH = os.getenv("GOOGLE_CALENDAR_CREDENTIALS_PATH", "./credentials/google_credentials.json")
    
    # Learn platform settings
    LEARN_USERNAME = os.getenv("LEARN_USERNAME")
    LEARN_PASSWORD = os.getenv("LEARN_PASSWORD")
    LEARN_BASE_URL = os.getenv("LEARN_BASE_URL", "https://learn.university.com")
    
    # Notification settings
    NOTIFICATION_ADVANCE_TIME = int(os.getenv("NOTIFICATION_ADVANCE_TIME", "24"))  # in hours
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Create a settings instance
settings = Settings()