from flask_restx import Namespace, Resource
from app.services.country_service import CountryService
#from app.persistence.data_manager import DataManager

countries = [
    {"code": "US", "name": "United States"},
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
]

# api = Namespace('countries', description='Country Operations')
# country_service = CountryService(DataManager())

#ns_countries = Namespace('countries', description='Country Operations')
#api.add_namespace(ns_countries)
api = Namespace('countries', description='Country Operations')

@api.route('/')
class CountryList(Resource):
    def get(self):
        """Retrieve all countries"""
        return countries, 200

@api.route('/<country_code>')
@api.param('country_code', 'The ISO country code')
class CountryResource(Resource):
    @api.doc('get_country')
    def get(self, country_code):
        """Retrieve details of a specific country by its country code."""
        country = next((c for c in countries if c['code'] == country_code), None)
        if not country:
            return {'error': 'Country not found'}, 404
        return country, 200

cities = [
    {"id": "1", "name": "New York", "country_code": "US"},
    {"id": "2", "name": "Los Angeles", "country_code": "US"},
    {"id": "3", "name": "Toronto", "country_code": "CA"},
    {"id": "4", "name": "Vancouver", "country_code": "CA"},
    {"id": "5", "name": "Mexico City", "country_code": "MX"},
    {"id": "6", "name": "Cancun", "country_code": "MX"},
    {"id": "7", "name": "San Juan", "country_code": "PR"},
    {"id": "8", "name": "London", "country_code": "GB"},
    {"id": "9", "name": "Manchester", "country_code": "GB"},
    {"id": "10", "name": "Berlin", "country_code": "DE"},
    {"id": "11", "name": "Munich", "country_code": "DE"},
    {"id": "12", "name": "Tokyo", "country_code": "JP"},
    {"id": "13", "name": "Osaka", "country_code": "JP"},
    {"id": "14", "name": "Paris", "country_code": "FR"},
    {"id": "15", "name": "Marseille", "country_code": "FR"},
    {"id": "16", "name": "Sydney", "country_code": "AU"},
    {"id": "17", "name": "Melbourne", "country_code": "AU"},
    {"id": "18", "name": "Sao Paulo", "country_code": "BR"},
    {"id": "19", "name": "Rio de Janeiro", "country_code": "BR"},
    {"id": "20", "name": "Mumbai", "country_code": "IN"},
    {"id": "21", "name": "Delhi", "country_code": "IN"},
    {"id": "22", "name": "Beijing", "country_code": "CN"},
    {"id": "23", "name": "Shanghai", "country_code": "CN"}
]

@api.route('/<country_code>/cities')
@api.param('country_code', 'The ISO country code')
class CityByCountry(Resource):
    def get(self, country_code):
        """Get cities by country code"""
        matching_cities = [city for city in cities if city['country_code'] == country_code]
        if not matching_cities:
            return {'error': 'No cities found for this country'}, 404
        return matching_cities, 200
