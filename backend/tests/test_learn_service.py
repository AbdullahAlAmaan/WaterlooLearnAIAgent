import unittest
from src.services.learn_service import LearnService

class TestLearnService(unittest.TestCase):
    
    def setUp(self):
        """Set up the LearnService instance for testing."""
        self.learn_service = LearnService()
    
    def test_initialize(self):
        """Test the initialization of the LearnService."""
        result = self.learn_service.initialize()
        self.assertTrue(result)  # Assuming it should return True on successful initialization

    def test_fetch_courses(self):
        """Test fetching courses from the Learn platform."""
        courses = self.learn_service.fetch_courses()
        self.assertIsInstance(courses, list)  # Expecting a list of courses

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()