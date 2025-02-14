from src.models.notification import Notification
from datetime import datetime

class NotificationService:
    def __init__(self):
        self.notifications = []  # List to hold Notification objects

    def create_notification(self, title: str, message: str, event_id: str, notify_time: datetime):
        """Create a new notification."""
        notification = Notification(
            id=self.generate_notification_id(),
            title=title,
            message=message,
            event_id=event_id,
            notify_time=notify_time
        )
        self.notifications.append(notification)
        return notification

    def send_notifications(self):
        """Send notifications that are due."""
        for notification in self.notifications:
            if not notification.is_sent and notification.notify_time <= datetime.now():
                notification.send()  # Call the send method to send the notification

    def generate_notification_id(self):
        """Generate a unique ID for the notification."""
        return f"notif-{len(self.notifications) + 1}"  # Simple ID generation logic
