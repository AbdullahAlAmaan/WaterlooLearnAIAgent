from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from src.config.settings import settings

class CalendarService:
    def __init__(self):
        self.creds = self.authenticate()

    def authenticate(self):
        """Authenticate with Google Calendar API."""
        creds = Credentials.from_authorized_user_file(settings.GOOGLE_CALENDAR_CREDENTIALS_PATH)
        return creds

    def create_event(self, event):
        """Create an event in Google Calendar."""
        service = build('calendar', 'v3', credentials=self.creds)
        event_body = {
            'summary': event.title,
            'start': {
                'dateTime': event.due_date,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': event.due_date,
                'timeZone': 'UTC',
            },
        }
        created_event = service.events().insert(calendarId='primary', body=event_body).execute()
        return created_event.get('id')  # Return the ID of the created event