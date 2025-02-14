from datetime import datetime

def format_datetime(dt: datetime) -> str:
    """Format a datetime object to a string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def parse_datetime(dt_str: str) -> datetime:
    """Parse a datetime string to a datetime object."""
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")