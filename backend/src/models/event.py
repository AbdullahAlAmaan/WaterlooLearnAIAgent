from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class Event:
    id: str
    title: str
    course_code: str
    due_date: datetime
    event_type: str  # 'quiz' or 'assignment'
    description: Optional[str] = None
    url: Optional[str] = None
    submission_type: Optional[str] = None
    is_synced: bool = False
    calendar_event_id: Optional[str] = None

@dataclass
class Assignment(Event):
    dropbox_id: Optional[str] = None
    max_attempts: Optional[int] = None
    file_types: Optional[List[str]] = None

@dataclass
class Quiz(Event):
    time_limit: Optional[int] = None  # in minutes
    num_questions: Optional[int] = None
    attempts_allowed: Optional[int] = None