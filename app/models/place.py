import uuid
from datetime import datetime

# I change city to city_id, and host for host_id 
class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, rooms, bathrooms, price_per_night, max_guests, amenities=[]):
        self.place_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities.copy()
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    '''
    For testing
    '''
    def __eq__(self, other):
        if not isinstance(other, Place):
            return NotImplemented
        return (self.name == other.name and
                self.description == other.description and
                self.address == other.address and
                self.city_id == other.city_id and
                self.latitude == other.latitude and
                self.longitude == other.longitude and
                self.host_id == other.host_id and
                self.rooms == other.rooms and
                self.bathrooms == other.bathrooms and
                self.price_per_night == other.price_per_night and
                self.max_guests == other.max_guests and
                self.amenities == other.amenities)
    # The method end here


    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
