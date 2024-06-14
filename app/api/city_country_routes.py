from flask_restx import Namespace, Resource
from app.services.city_service import CityService
from app.services.country_service import CountryService
from app.persistence.data_manager import DataManager

api = Namespace('locations', description='Location operations')

# Initialize both services with DataManager
data_manager = DataManager()
city_service = CityService(data_manager)
country_service = CountryService(data_manager)


@api.route('/countries')
class CountryList(Resource):
    def get(self):
        """Get a list of all countries."""
        countries = country_service.get_all_countries()
        return [country.to_dict() for country in countries], 200

@api.route('/countries/<country_code>/cities')
@api.param('country_code', 'The ISO country code')
class CityByCountry(Resource):
    def get(self, country_code):
        """Get cities by country code."""
        country = country_service.get_country(country_code)
        if not country:
            return {'error': 'Country not found'}, 404
        return [city.to_dict() for city in country.cities], 200

@api.route('/cities')
class CityList(Resource):
    def post(self):
        """Create a new city"""
        data = api.payload
        try:
            city = city_service.create_city(data['name'], data['country_code'])
            return city.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

@api.route('/cities/<city_id>')
@api.param('city_id', 'The city identifier')
class CityResource(Resource):
    def get(self, city_id):
        """Get a city by ID"""
        try:
            city = city_service.get_city(city_id)
            return city.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    def put(self, city_id):
        """Update a city by ID"""
        data = api.payload
        try:
            city = city_service.update_city(city_id, data['name'])
            return city.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    def delete(self, city_id):
        """Delete a city by ID"""
        try:
            city_service.delete_city(city_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404
