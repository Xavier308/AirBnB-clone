import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.country_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = [] 

    def add_city(self, city):
        """Adds a city to the country."""
        self.cities.append(city)

    def to_dict(self):
        return {
            "country_id": self.country_id,
            "code": self.code,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "cities": [city.to_dict() for city in self.cities]
        }

    def __eq__(self, other):
        if not isinstance(other, Country):
            return NotImplemented
        return self.country_id == other.country_id
