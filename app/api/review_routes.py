from flask_restx import Namespace, Resource
from app.services.review_service import ReviewService
from app.persistence.data_manager import DataManager

api = Namespace('reviews', description='Review operations')
review_service = ReviewService(DataManager())

@api.route('/places/<place_id>/reviews')
@api.param('place_id', 'The place identifier')
class ReviewByPlace(Resource):
    @api.doc('create_review')
    def post(self, place_id):
        """Create a review for a place"""
        data = api.payload
        try:
            review = review_service.create_review(place_id, data['user_id'], data['rating'], data['comment'])
            return review.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('get_reviews_by_place')
    def get(self, place_id):
        """Get reviews by place ID"""
        reviews = review_service.get_reviews_by_place(place_id)
        return [review.to_dict() for review in reviews], 200

@api.route('/users/<user_id>/reviews')
@api.param('user_id', 'The user identifier')
class ReviewByUser(Resource):
    @api.doc('get_reviews_by_user')
    def get(self, user_id):
        """Get reviews by user ID"""
        reviews = review_service.get_reviews_by_user(user_id)
        return [review.to_dict() for review in reviews], 200

@api.route('/<review_id>')
@api.param('review_id', 'The review identifier')
class Review(Resource):
    @api.doc('get_review')
    def get(self, review_id):
        """Get a single review by ID"""
        try:
            review = review_service.get_review(review_id)
            return review.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @api.doc('update_review')
    def put(self, review_id):
        """Update a review by ID"""
        data = api.payload
        try:
            review = review_service.update_review(review_id, data['rating'], data['comment'])
            return review.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('delete_review')
    def delete(self, review_id):
        """Delete a review by ID"""
        try:
            review_service.delete_review(review_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404
