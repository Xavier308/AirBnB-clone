import uuid
from datetime import datetime

class City:
    def __init__(self, name, country):
        self.city_id = str(uuid.uuid4())
        self.name = name
        self.country = country  # This should be a Country object
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __eq__(self, other):
        if not isinstance(other, City):
            return NotImplemented
        return (self.name == other.name and
                self.country == other.country)
