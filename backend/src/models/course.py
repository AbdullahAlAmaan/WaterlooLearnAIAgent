from dataclasses import dataclass
from typing import List
from .event import Event

@dataclass
class Course:
    id: str
    code: str
    name: str
    url: str
    is_active: bool = True
    term: Optional[str] = None
    events: List[Event] = None  # List of events associated with the course

    def __post_init__(self):
        if self.events is None:
            self.events = []

    def add_event(self, event: Event):
        """Add an event to the course."""
        self.events.append(event)

    def get_upcoming_events(self):
        """Get upcoming events for the course."""
        return [e for e in self.events if e.due_date > datetime.now()]