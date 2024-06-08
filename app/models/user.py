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
