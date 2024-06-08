def format_datetime(value, format='%Y-%m-%d %H:%M'):
    """Format a datetime to a more readable form."""
    if value:
        return value.strftime(format)
    return ""

def calculate_age(birthdate):
    """Calculate age from a birthdate."""
    from datetime import datetime, date
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
