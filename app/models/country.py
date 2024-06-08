import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.country_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = []  # Initialize an empty list to hold City objects

    def add_city(self, city):
        """Adds a city to the country."""
        self.cities.append(city)
