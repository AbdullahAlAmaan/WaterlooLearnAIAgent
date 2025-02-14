import requests
from src.config.settings import settings
from src.models.event import Event

class SubmissionService:
    def __init__(self):
        self.submissions = []  # List to hold submission records

    def submit_assignment(self, event: Event, file_path: str):
        """Submit an assignment to the Learn platform."""
        url = f"{settings.LEARN_BASE_URL}/submit_assignment"  # Replace with actual submission endpoint
        files = {'file': open(file_path, 'rb')}
        data = {
            'event_id': event.id,
            'course_code': event.course_code,
            'submission_type': event.submission_type
        }

        response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            submission_record = {
                'event_id': event.id,
                'status': 'submitted',
                'response': response.json()
            }
            self.submissions.append(submission_record)
            return submission_record
        else:
            raise Exception(f"Failed to submit assignment: {response.status_code} - {response.text}")

    def submit_quiz(self, event: Event, answers: dict):
        """Submit a quiz to the Learn platform."""
        url = f"{settings.LEARN_BASE_URL}/submit_quiz"  # Replace with actual quiz submission endpoint
        data = {
            'event_id': event.id,
            'course_code': event.course_code,
            'answers': answers
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            submission_record = {
                'event_id': event.id,
                'status': 'submitted',
                'response': response.json()
            }
            self.submissions.append(submission_record)
            return submission_record
        else:
            raise Exception(f"Failed to submit quiz: {response.status_code} - {response.text}")