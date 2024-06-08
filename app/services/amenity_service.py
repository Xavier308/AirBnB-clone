from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager

class AmenityService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def create_amenity(self, name):
        if self.data_manager.get_by_name(name, Amenity):
            raise ValueError("An amenity with this name already exists.")
        amenity = Amenity(name=name)
        self.data_manager.save(amenity)
        return amenity

    def update_amenity(self, amenity_id, name):
        amenity = self.data_manager.get(amenity_id, Amenity)
        if not amenity:
            raise ValueError("Amenity not found.")
        amenity.name = name
        self.data_manager.update(amenity)
        return amenity

    def delete_amenity(self, amenity_id):
        amenity = self.data_manager.get(amenity_id, Amenity)
        if not amenity:
            raise ValueError("Amenity not found.")
        self.data_manager.delete(amenity_id, Amenity)

    def get_amenity(self, amenity_id):
        amenity = self.data_manager.get(amenity_id, Amenity)
        if not amenity:
            raise ValueError("Amenity not found.")
        return amenity

    def get_all_amenities(self):
        return self.data_manager.get_all(Amenity)
