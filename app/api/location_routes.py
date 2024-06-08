from flask_restx import Namespace, Resource
from app.services.city_service import CityService
from app.persistence.data_manager import DataManager

api = Namespace('locations', description='Location operations')
city_service = CityService(DataManager())

@api.route('/countries')
class CountryList(Resource):
    def get(self):
        """Get a list of countries"""
        countries = [{'name': 'Country1', 'code': 'C1'}, {'name': 'Country2', 'code': 'C2'}]  # Example static data
        return countries, 200

@api.route('/countries/<country_code>/cities')
@api.param('country_code', 'The ISO country code')
class CityByCountry(Resource):
    def get(self, country_code):
        """Get cities by country code"""
        cities = city_service.get_all_cities()  # You would filter by country code in real implementation
        return [city.to_dict() for city in cities], 200

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
