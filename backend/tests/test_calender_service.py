import unittest
from src.services.calendar_service import CalendarService

class TestCalendarService(unittest.TestCase):
    
    def setUp(self):
        """Set up the CalendarService instance for testing."""
        self.calendar_service = CalendarService()
    
    def test_initialize(self):
        """Test the initialization of the CalendarService."""
        result = self.calendar_service.initialize()
        self.assertTrue(result)  # Assuming it should return True on successful initialization

    def test_create_event(self):
        """Test creating an event in Google Calendar."""
        event = {
            'summary': 'Test Event',
            'start': {'dateTime': '2023-10-01T10:00:00Z'},
            'end': {'dateTime': '2023-10-01T11:00:00Z'},
        }
        result = self.calendar_service.create_event(event)
        self.assertTrue(result)  # Assuming it should return True on successful event creation

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()