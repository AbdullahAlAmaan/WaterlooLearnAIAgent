from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    event_type: str  # 'quiz', 'submission', or 'other'
    course_id: Optional[str] = None
    submission_url: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: str
    
    class Config:
        from_attributes = True