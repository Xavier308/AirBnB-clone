from flask_restx import Namespace, Resource
from app.services.amenity_service import AmenityService
from app.persistence.data_manager import DataManager

api = Namespace('amenities', description='Amenity operations')
amenity_service = AmenityService(DataManager())

@api.route('/')
class AmenityList(Resource):
    @api.doc('create_amenity')
    def post(self):
        """Create a new amenity"""
        data = api.payload  # Use api.payload instead of request.get_json()
        try:
            amenity = amenity_service.create_amenity(data['name'])
            return amenity.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 409

    @api.doc('get_amenities')
    def get(self):
        """Get all amenities"""
        amenities = amenity_service.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
class Amenity(Resource):
    @api.doc('get_amenity')
    def get(self, amenity_id):
        """Get an amenity by ID"""
        try:
            amenity = amenity_service.get_amenity(amenity_id)
            return amenity.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @api.doc('update_amenity')
    def put(self, amenity_id):
        """Update an amenity by ID"""
        data = api.payload
        try:
            amenity = amenity_service.update_amenity(amenity_id, data['name'])
            return amenity.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('delete_amenity')
    def delete(self, amenity_id):
        """Delete an amenity by ID"""
        try:
            amenity_service.delete_amenity(amenity_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404
