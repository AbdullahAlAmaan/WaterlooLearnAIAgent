import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # API Settings
    API_V1_PREFIX = "/api/v1"
    PROJECT_NAME = "Calendar Assistant"
    
    # Calendar Settings
    GOOGLE_CALENDAR_CREDENTIALS_PATH = os.getenv("GOOGLE_CALENDAR_CREDENTIALS_PATH")
    
    # Database Settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./calendar_assistant.db")
    
    # OpenAI Settings (for later use)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()