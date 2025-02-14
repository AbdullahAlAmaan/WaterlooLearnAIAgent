import unittest
from src.services.quiz_service import QuizService

class TestQuizService(unittest.TestCase):
    
    def setUp(self):
        """Set up the QuizService instance for testing."""
        self.quiz_service = QuizService()
    
    def test_prepare_quiz_materials(self):
        """Test preparing quiz materials."""
        quiz = {'id': 'quiz1', 'title': 'Sample Quiz'}
        course = {'id': 'course1', 'name': 'Sample Course'}
        result = self.quiz_service.prepare_quiz_materials(quiz, course)
        self.assertIsInstance(result, dict)  # Expecting a dictionary of materials

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()