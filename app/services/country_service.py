from app.models.country import Country
from app.persistence.data_manager import DataManager

class CountryService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def get_country(self, country_id):
        """Retrieve a country by its ID."""
        return self.data_manager.get(country_id, Country)

    def get_all_countries(self):
        """Retrieve all countries."""
        return self.data_manager.get_all(Country)
