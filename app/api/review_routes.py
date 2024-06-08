from flask import Blueprint, request, jsonify
from app.services.review_service import ReviewService
from app.persistence.data_manager import DataManager

review_routes = Blueprint('review_routes', __name__)
review_service = ReviewService(DataManager())

@review_routes.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    try:
        review = review_service.create_review(place_id, data['user_id'], data['rating'], data['comment'])
        return jsonify(review.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@review_routes.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    reviews = review_service.get_reviews_by_user(user_id)
    return jsonify([review.to_dict() for review in reviews]), 200

@review_routes.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    reviews = review_service.get_reviews_by_place(place_id)
    return jsonify([review.to_dict() for review in reviews]), 200

@review_routes.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    try:
        review = review_service.get_review(review_id)
        return jsonify(review.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@review_routes.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    try:
        review = review_service.update_review(review_id, data['rating'], data['comment'])
        return jsonify(review.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@review_routes.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        review_service.delete_review(review_id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
