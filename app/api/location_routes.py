from flask import Blueprint, request, jsonify
from app.services.city_service import CityService
from app.persistence.data_manager import DataManager

location_routes = Blueprint('location_routes', __name__)
city_service = CityService(DataManager())

@location_routes.route('/countries', methods=['GET'])
def get_countries():
    countries = [{'name': 'Country1', 'code': 'C1'}, {'name': 'Country2', 'code': 'C2'}]  # Example static data
    return jsonify(countries), 200

@location_routes.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    cities = city_service.get_all_cities()  # You would filter by country code in real implementation
    return jsonify([city.to_dict() for city in cities]), 200

@location_routes.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    try:
        city = city_service.create_city(data['name'], data['country_code'])
        return jsonify(city.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@location_routes.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    try:
        city = city_service.get_city(city_id)
        return jsonify(city.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@location_routes.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    try:
        city = city_service.update_city(city_id, data['name'])
        return jsonify(city.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@location_routes.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    try:
        city_service.delete_city(city_id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
