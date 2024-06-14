from flask_restx import Namespace, Resource
from app.services.country_service import CountryService
from app.persistence.data_manager import DataManager

api = Namespace('countries', description='Country Operations')
country_service = CountryService(DataManager())

@api.route('/')
class CountryList(Resource):
    def get(self):
        """Retrieve all countries"""
        countries = country_service.get_all_countries()
        return [country.to_dict() for country in countries], 200

@api.route('/<country_code>')
@api.param('country_code', 'The ISO country code')
class CountryResource(Resource):
    @api.doc('get_country')
    def get(self, country_code):
        """Retrieve details of a specific country by its country code."""
        country = country_service.get_country(country_code)
        if not country:
            return {'error': 'Country not found'}, 404
        return country.to_dict(), 200

@api.route('/<country_code>/cities')
@api.param('country_code', 'The ISO country code')
class CityByCountry(Resource):
    def get(self, country_code):
        """Get cities by country code"""
        country = country_service.get_country(country_code)
        if not country:
            return {'error': 'Country not found'}, 404
        return [city.to_dict() for city in country.cities], 200
