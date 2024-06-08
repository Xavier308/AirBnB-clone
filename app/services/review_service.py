from app.models.review import Review
from app.persistence.data_manager import DataManager
from app.models.user import User
from app.models.place import Place


class ReviewService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def create_review(self, place_id, user_id, rating, comment):
        # Validation for user and place existence and rating within bounds
        if not self.data_manager.get(user_id, User):
            raise ValueError("User not found.")
        if not self.data_manager.get(place_id, Place):
            raise ValueError("Place not found.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        review = Review(place_id=place_id, user_id=user_id, rating=rating, comment=comment)
        self.data_manager.save(review)
        return review

    def update_review(self, review_id, rating, comment):
        review = self.data_manager.get(review_id, Review)
        if not review:
            raise ValueError("Review not found.")
        
        review.rating = rating
        review.comment = comment
        self.data_manager.update(review)
        return review

    def delete_review(self, review_id):
        review = self.data_manager.get(review_id, Review)
        if not review:
            raise ValueError("Review not found.")
        self.data_manager.delete(review_id, Review)

    def get_review(self, review_id):
        review = self.data_manager.get(review_id, Review)
        if not review:
            raise ValueError("Review not found.")
        return review

    def get_reviews_by_user(self, user_id):
        # Implement logic to retrieve all reviews by a user
        return self.data_manager.get_all_by_user_id(user_id, Review)

    def get_reviews_by_place(self, place_id):
        # Implement logic to retrieve all reviews for a place
        return self.data_manager.get_all_by_place_id(place_id, Review)
