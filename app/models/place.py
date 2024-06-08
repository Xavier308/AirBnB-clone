import uuid
from datetime import datetime


class Place:
    def __init__(self, name, description, address, city, host, rooms, price_per_night, max_guests, amenities=[]):
        self.place_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.host = host  # This should be a User object
        self.rooms = rooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities.copy()  # Make a copy of the list to avoid mutable default argument issues
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
