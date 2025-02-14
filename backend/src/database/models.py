from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(String, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    term = Column(String)
    
    events = relationship("EventModel", back_populates="course")

class EventModel(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(String, ForeignKey("courses.id"))
    due_date = Column(DateTime, nullable=False)
    event_type = Column(String, nullable=False)  # 'quiz' or 'assignment'
    description = Column(String)
    url = Column(String)
    submission_type = Column(String)
    is_synced = Column(Boolean, default=False)
    calendar_event_id = Column(String)
    
    course = relationship("CourseModel", back_populates="events")

    # Additional fields for quizzes
    time_limit = Column(Integer)
    num_questions = Column(Integer)
    attempts_allowed = Column(Integer)

    # Additional fields for assignments
    dropbox_id = Column(String)
    max_attempts = Column(Integer)
    file_types = Column(String)  # Stored as JSON string