from flask_restx import Namespace, Resource, fields, reqparse
from app.services.city_service import CityService
from app.services.country_service import CountryService
from app.persistence.data_manager import DataManager


api = Namespace('cities', description='City Operations')

# Initialize DataManager
data_manager = DataManager()

# Initialize CountryService
country_service = CountryService(data_manager)

# Initialize CityService with both DataManager and CountryService
city_service = CityService(data_manager, country_service)

city_model = api.model('City', {
    'id': fields.String(description='The unique identifier of the city'),
    'name': fields.String(required=True, description='Name of the city'),
    'country_code': fields.String(required=True, description='Country ISO alpha-2 code'),
    'created_at': fields.DateTime(description='Timestamp city was created'),
    'updated_at': fields.DateTime(description='Timestamp city was last updated')
})

city_parser = reqparse.RequestParser()
city_parser.add_argument('name', type=str, required=True, help='Name of the city cannot be blank')
city_parser.add_argument('country_code', type=str, required=True, help='Country ISO code cannot be blank')

@api.route('/')
class CityList(Resource):
    @api.doc('get_all_cities')
    @api.marshal_with(city_model, as_list=True)
    def get(self):
        """Retrieve all cities"""
        cities = city_service.get_all_cities()
        if not cities:
            return {'message': 'No cities found'}, 404
        return cities if cities else [], 200  # Ensure to return an empty list with a 200 status if no cities are found


    @api.doc('create_city')
    @api.expect(city_parser)
    def post(self):
        """Create a new city"""
        data = city_parser.parse_args()
        if not country_service.is_valid_country(data['country_code']):
            return {"message": "Invalid country code provided"}, 400
        if city_service.is_duplicate_city(data['name'], data['country_code']):
            return {"message": "Duplicate city name within the same country"}, 409
        city = city_service.create_city(data['name'], data['country_code'])
        return api.marshal(city, city_model), 201


@api.route('/<string:city_id>')
@api.param('city_id', 'The city identifier')
@api.response(404, 'City not found')
class CityResource(Resource):
    @api.doc('get_city')
    @api.marshal_with(city_model)
    def get(self, city_id):
        """Get a city by ID"""
        city = city_service.get_city(city_id)
        if not city:
            api.abort(404)
        return city

    @api.doc('update_city')
    @api.expect(city_parser)
    def put(self, city_id):
        """Update a city by ID"""
        data = city_parser.parse_args()
        city = city_service.update_city(city_id, **data)
        if not city:
            api.abort(404)
        return api.marshal(city, city_model), 200

    @api.doc('delete_city')
    def delete(self, city_id):
        """Delete a city by ID"""
        if not city_service.delete_city(city_id):
            api.abort(404)
        return '', 204
