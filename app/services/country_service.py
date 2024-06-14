from app.models.country import Country
from app.persistence.data_manager import DataManager

class CountryService:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        # Assuming a static list of countries is part of CountryService
        self.countries = [
            {"code": "CA", "name": "Canada"},
            {"code": "MX", "name": "Mexico"},
            {"code": "PR", "name": "Puerto Rico"},
            {"code": "GB", "name": "United Kingdom"},
            {"code": "DE", "name": "Germany"},
            {"code": "JP", "name": "Japan"},
            {"code": "FR", "name": "France"},
            {"code": "AU", "name": "Australia"},
            {"code": "BR", "name": "Brazil"},
            {"code": "IN", "name": "India"},
            {"code": "CN", "name": "China"}
            # other countries
        ]
    
    def is_valid_country(self, country_code):
        """Check if a given country code exists in the static list."""
        return any(country['code'] == country_code for country in self.countries)

    def get_country(self, country_code):
        """Retrieve a country by its ISO code from the static list."""
        return next((country for country in self.countries if country['code'] == country_code), None)

    def get_all_countries(self):
        """Retrieve all countries from the static list."""
        return self.countries
    
    
    '''
    def is_valid_country(self, country_code):
        """Validate the country code."""
        return any(country['code'] == country_code for country in self.data_manager.get_all_countries())
    
    def get_country(self, country_id):
        """Retrieve a country by its ID."""
        return self.data_manager.get(country_id, Country)

    def get_all_countries(self):
        """Retrieve all countries."""
        return self.data_manager.get_all(Country)
    '''
