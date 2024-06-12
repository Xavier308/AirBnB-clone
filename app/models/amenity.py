import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name): # I delete country
        self.amenity_id = str(uuid.uuid4())
        self.name = name
        # self.country = country  # This should be a Country object
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __eq__(self, other):
        if not isinstance(other, Amenity):
            return NotImplemented
        return self.name == other.name
