import requests
from src.config.settings import settings
from src.models.quiz import Quiz
from src.models.course import Course

class QuizService:
    def __init__(self):
        self.quizzes = []  # List to hold Quiz objects

    def generate_mock_test(self, course: Course):
        """Generate a custom mock test based on course notes using DeepSeek API."""
        # Fetch course notes (this could be a method that scrapes or retrieves notes)
        course_notes = self.fetch_course_notes(course)

        # Pass the notes to DeepSeek API to generate a mock test
        quiz = self.fetch_quiz_from_deepseek(course_notes)

        # Add the quiz to the list of quizzes
        self.quizzes.append(quiz)
        return quiz

    def fetch_course_notes(self, course: Course):
        """Fetch course notes for the given course."""
        # Logic to scrape or retrieve course notes
        # For now, we'll return mock notes
        return [
            "Note 1: Important concept about algorithms.",
            "Note 2: Overview of data structures.",
            "Note 3: Key points on software engineering."
        ]

    def fetch_quiz_from_deepseek(self, course_notes):
        """Send course notes to DeepSeek API to generate a mock test."""
        url = f"{settings.DEEPSKEE_API_URL}/generate_quiz"  # Replace with actual DeepSeek API endpoint
        payload = {
            'notes': course_notes,
            'api_key': settings.DEEPSKEE_API_KEY  # Assuming you have an API key
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            quiz_data = response.json()
            quiz = Quiz(
                id=quiz_data['id'],
                title=quiz_data['title'],
                course_code=quiz_data['course_code'],
                due_date=quiz_data['due_date'],
                event_type='quiz',
                num_questions=quiz_data.get('num_questions'),
                attempts_allowed=quiz_data.get('attempts_allowed')
            )
            return quiz
        else:
            raise Exception(f"Failed to generate quiz: {response.status_code} - {response.text}")