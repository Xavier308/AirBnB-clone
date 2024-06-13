import uuid
from datetime import datetime

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

    def add_place(self, place):
        self.places.append(place)

    # Added to resolve problem in live testing API - **pending...
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,  # You might want to hash the password before saving
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'places': [place.to_dict() for place in self.places]  # Assuming Place has a to_dict method
        }