from flask import Blueprint, request, jsonify
from app.services.place_service import PlaceService
from app.persistence.data_manager import DataManager

place_routes = Blueprint('place_routes', __name__)
place_service = PlaceService(DataManager())

@place_routes.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    try:
        place = place_service.create_place(**data)
        return jsonify(place.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@place_routes.route('/places', methods=['GET'])
def get_places():
    places = place_service.get_all_places()
    return jsonify([place.to_dict() for place in places]), 200

@place_routes.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    try:
        place = place_service.get_place(place_id)
        return jsonify(place.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@place_routes.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    try:
        place = place_service.update_place(place_id, **data)
        return jsonify(place.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@place_routes.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    try:
        place_service.delete_place(place_id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
