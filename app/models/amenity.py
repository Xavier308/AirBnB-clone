import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name, country):
        self.amenity_id = str(uuid.uuid4())
        self.name = name
        self.country = country  # This should be a Country object
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
