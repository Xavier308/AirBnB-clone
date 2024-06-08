from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.persistence.data_manager import DataManager
from email_validator import validate_email, EmailNotValidError

user_routes = Blueprint('user_routes', __name__)
user_service = UserService(DataManager())

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = user_service.create_user(data['email'], data['first_name'], data['last_name'])
        return jsonify(user.to_dict()), 201
    except EmailNotValidError:
        return jsonify({"error": "Invalid email format"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        user = user_service.update_user(user_id, **data)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return '', 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
