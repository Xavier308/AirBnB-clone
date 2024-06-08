from flask import Blueprint, request, jsonify
from app.services.amenity_service import AmenityService
from app.persistence.data_manager import DataManager

amenity_routes = Blueprint('amenity_routes', __name__)
amenity_service = AmenityService(DataManager())

@amenity_routes.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    try:
        amenity = amenity_service.create_amenity(data['name'])
        return jsonify(amenity.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 409

@amenity_routes.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = amenity_service.get_all_amenities()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@amenity_routes.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    try:
        amenity = amenity_service.get_amenity(amenity_id)
        return jsonify(amenity.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@amenity_routes.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    try:
        amenity = amenity_service.update_amenity(amenity_id, data['name'])
        return jsonify(amenity.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@amenity_routes.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        amenity_service.delete_amenity(amenity_id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
