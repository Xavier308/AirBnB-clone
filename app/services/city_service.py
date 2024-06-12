from app.models.city import City
from app.persistence.data_manager import DataManager

class CityService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def create_city(self, name, country):
        if self.data_manager.get(city_name=name, country=country):
            raise ValueError("City with this name already exists in the specified country.")
        city = City(name=name, country=country)
        self.data_manager.save(city)
        return city

    def update_city(self, city_id, name):
        city = self.data_manager.get(city_id, City)
        if not city:
            raise ValueError("City not found.")
        city.name = name
        self.data_manager.update(city)
        return city

    def delete_city(self, city_id):
        city = self.data_manager.get(city_id, City)
        if not city:
            raise ValueError("City not found.")
        self.data_manager.delete(city_id, City)

    def get_city(self, city_id):
        city = self.data_manager.get(city_id, City)
        if not city:
            raise ValueError("City not found.")
        return city

    def get_all_cities(self):
        return self.data_manager.get_all(City)
