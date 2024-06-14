from app.models.city import City
from app.persistence.data_manager import DataManager

class CityService:
    def __init__(self, data_manager, country_service):
        self.data_manager = data_manager
        self.country_service = country_service

    def create_city(self, name, country_code):
        # Check if the country code is valid
        if not self.country_service.is_valid_country(country_code):
            raise ValueError("Country code is invalid.")

        # Ensure no duplicate city name exists within the same country
        if self.is_duplicate_city(name, country_code):
            raise ValueError("City with this name already exists in the specified country.")

        # Create the city if validation passes
        city = City(name=name, country_code=country_code)
        self.data_manager.save(city)
        return city

    def update_city(self, city_id, name, country_code):
        city = self.data_manager.get(city_id, City)
        if not city:
            raise ValueError("City not found.")

        # Check if updating to a new name that already exists in the same country
        if self.is_duplicate_city(name, country_code, city_id):
            raise ValueError("Another city with this name already exists in the specified country.")

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
        """Retrieve all cities from the DataManager and return them as City objects."""
        city_data = self.data_manager.get_all('City')
        return [City(**data) for data in city_data]

    def is_duplicate_city(self, name, country_code, city_id=None):
        """Use direct database query to check for city name uniqueness within the same country."""
        query_conditions = [City.name == name, City.country_code == country_code]
        if city_id:
            query_conditions.append(City.id != city_id)
        return self.data_manager.exists(City, *query_conditions)
