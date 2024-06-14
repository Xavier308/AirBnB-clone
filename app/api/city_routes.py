from flask_restx import Namespace, Resource
from app.services.city_service import CityService
from app.services.country_service import CountryService # I added this because the app do not initialize
from app.persistence.data_manager import DataManager

api = Namespace('cities', description='City Operations')
city_service = CityService(DataManager(), CountryService) # I added CountryService

@api.route('/')
class CityList(Resource):
    def get(self):
        """Retrieve all cities"""
        cities = city_service.get_all_cities()
        return [city.to_dict() for city in cities], 200

    def post(self):
        """Create a new city"""
        data = api.payload
        city = city_service.create_city(data['name'], data['country_code'])
        return city.to_dict(), 201

@api.route('/<city_id>')
@api.param('city_id', 'The city identifier')
class CityResource(Resource):
    def get(self, city_id):
        """Get a city by ID"""
        city = city_service.get_city(city_id)
        return city.to_dict(), 200

    def put(self, city_id):
        """Update a city by ID"""
        data = api.payload
        city = city_service.update_city(city_id, **data)
        return city.to_dict(), 200

    def delete(self, city_id):
        """Delete a city by ID"""
        city_service.delete_city(city_id)
        return '', 204
