import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, first_name, last_name, user_id=None, created_at=None, updated_at=None, places=None):
        self.user_id = user_id if user_id else str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = self.parse_datetime(created_at)
        self.updated_at = self.parse_datetime(updated_at)
        self.places = places if places else []

    def add_place(self, place):
        self.places.append(place)

    def parse_datetime(self, date_str):
        if isinstance(date_str, str):
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        return date_str or datetime.now()

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'places': [place.to_dict() for place in self.places]  # Assuming Place has a to_dict method
        }
    
    '''
class User:
    def __init__(self, email, password, first_name, last_name):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []  # This will hold references to places hosted by the user
'''