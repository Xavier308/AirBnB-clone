from app.models.place import Place
from app.persistence.data_manager import DataManager
from app.models.city import City # check this later

class PlaceService:
    def __init__(self, data_manager):
        self.data_manager = data_manager
    # comment
    def create_place(self, name, description, address, city_id, latitude, longitude, host_id, rooms, bathrooms, price_per_night, max_guests, amenities):
        # Validations (simplified for brevity)
        if self.data_manager.get(city_id, City) is None:
            raise ValueError("City does not exist.")
        
        # Further validation for amenities, numbers, etc.

        place = Place(name=name, description=description, address=address, city_id=city_id, 
                      latitude=latitude, longitude=longitude, host_id=host_id, rooms=rooms, 
                      bathrooms=bathrooms, price_per_night=price_per_night, max_guests=max_guests, amenities=amenities)
        self.data_manager.save(place)
        return place

    def update_place(self, place_id, **kwargs):
        place = self.data_manager.get(place_id, Place)
        if not place:
            raise ValueError("Place not found.")
        
        # Update properties
        for key, value in kwargs.items():
            setattr(place, key, value)
        
        self.data_manager.update(place)
        return place

    def get_place(self, place_id):
        place = self.data_manager.get(place_id, Place)
        if not place:
            raise ValueError("Place not found.")
        return place

    def delete_place(self, place_id):
        self.data_manager.delete(place_id, Place)

    def get_all_places(self):
        return self.data_manager.get_all(Place)
