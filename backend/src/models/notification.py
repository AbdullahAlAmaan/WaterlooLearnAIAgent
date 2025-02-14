from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Notification:
    id: str
    title: str
    message: str
    event_id: str  # The ID of the associated event
    notify_time: datetime  # When to send the notification
    is_sent: bool = False  # Status of the notification

    def send(self):
        """Send the notification."""
        # Logic to send the notification (e.g., email, push notification)
        print(f"Sending notification: {self.title} - {self.message}")
        self.is_sent = True

    def __post_init__(self):
        """Ensure notify_time is in the future."""
        if self.notify_time <= datetime.now():
            raise ValueError("Notification time must be in the future.")