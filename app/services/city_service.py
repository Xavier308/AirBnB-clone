from app.models.city import City
from app.persistence.data_manager import DataManager


class CityService:
    def __init__(self, data_manager, country_service):
        self.data_manager = data_manager
        self.country_service = country_service

    def create_city(self, name, country_code):
        country = self.country_service.get_country(country_code)
        if not country:
            raise ValueError("Country code is invalid.")

        existing_city = self.data_manager.get(city_name=name, country=country_code)
        if existing_city:
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
