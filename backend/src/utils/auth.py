from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from src.config.settings import settings

def authenticate_google_calendar():
    """Authenticate with Google Calendar API and return credentials."""
    creds = None
    try:
        creds = Credentials.from_authorized_user_file(settings.GOOGLE_CALENDAR_CREDENTIALS_PATH)
    except Exception as e:
        print(f"Error loading credentials: {e}")
        flow = InstalledAppFlow.from_client_secrets_file(
            settings.GOOGLE_CALENDAR_CREDENTIALS_PATH,
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        creds = flow.run_local_server(port=0)
    return creds