from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
from datetime import datetime
from typing import List, Optional
from ..models.event import Event

class CalendarService:
    def __init__(self, credentials_path: str):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        self.credentials_path = credentials_path
        self.service = self._get_calendar_service()

    def _get_calendar_service(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return build('calendar', 'v3', credentials=creds)

    async def get_upcoming_events(self) -> List[Event]:
        try:
            now = datetime.utcnow().isoformat() + 'Z'
            events_result = self.service.events().list(
                calendarId='primary',
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            return [
                Event(
                    id=event['id'],
                    title=event.get('summary', ''),
                    description=event.get('description', ''),
                    start_time=datetime.fromisoformat(
                        event['start'].get('dateTime', event['start'].get('date'))
                    ),
                    event_type=self._determine_event_type(event),
                    course_id=self._extract_course_id(event),
                    submission_url=self._extract_submission_url(event)
                )
                for event in events_result.get('items', [])
            ]
        except Exception as e:
            print(f"Error fetching events: {e}")
            return []

    def _determine_event_type(self, event: dict) -> str:
        title = event.get('summary', '').lower()
        if any(word in title for word in ['quiz', 'exam', 'test']):
            return 'quiz'
        elif any(word in title for word in ['submission', 'assignment', 'project']):
            return 'submission'
        return 'other'

    def _extract_course_id(self, event: dict) -> Optional[str]:
        # TODO: Implement based on your calendar event format
        return None

    def _extract_submission_url(self, event: dict) -> Optional[str]:
        # TODO: Implement based on your calendar event format
        return None