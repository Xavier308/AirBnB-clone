from flask_restx import Namespace, Resource
from app.services.place_service import PlaceService
from app.persistence.data_manager import DataManager

api = Namespace('places', description='Place operations')
place_service = PlaceService(DataManager())

@api.route('/')
class PlaceList(Resource):
    @api.doc('create_place')
    def post(self):
        """Create a new place"""
        data = api.payload  # Use api.payload instead of request.get_json()
        try:
            place = place_service.create_place(**data)
            return place.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('get_places')
    def get(self):
        """Get all places"""
        places = place_service.get_all_places()
        return [place.to_dict() for place in places], 200

@api.route('/<place_id>')
@api.param('place_id', 'The place identifier')
class Place(Resource):
    @api.doc('get_place')
    def get(self, place_id):
        """Get a place by ID"""
        try:
            place = place_service.get_place(place_id)
            return place.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @api.doc('update_place')
    def put(self, place_id):
        """Update a place by ID"""
        data = api.payload
        try:
            place = place_service.update_place(place_id, **data)
            return place.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('delete_place')
    def delete(self, place_id):
        """Delete a place by ID"""
        try:
            place_service.delete_place(place_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404
