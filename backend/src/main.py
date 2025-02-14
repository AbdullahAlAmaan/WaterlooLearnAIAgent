import logging
from src.utils.logging_config import setup_logging
from src.services.learn_service import LearnService
from src.services.calendar_service import CalendarService
from src.services.quiz_service import QuizService
from src.services.submission_service import SubmissionService
from src.services.notification_service import NotificationService

def main():
    """Main entry point for the application."""
    setup_logging()  # Set up logging configuration
    logging.info("Application started.")

    # Initialize services
    learn_service = LearnService()
    calendar_service = CalendarService()
    quiz_service = QuizService()
    submission_service = SubmissionService()
    notification_service = NotificationService()

    # Example usage of services
    try:
        learn_service.initialize()
        courses = learn_service.fetch_courses()
        logging.info(f"Fetched courses: {courses}")

        # Generate a mock test for the first course
        if courses:
            quiz = quiz_service.generate_mock_test(courses[0])
            logging.info(f"Generated quiz: {quiz}")

        # Additional logic for calendar, submissions, and notifications can be added here

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()