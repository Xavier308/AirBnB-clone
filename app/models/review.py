import uuid
from datetime import datetime

class Review:
    def __init__(self, user, place, text, rating):
        self.review_id = str(uuid.uuid4())
        self.user = user  # This should be a User object
        self.place = place  # This should be a Place object
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        # Automatically add this review to the place's list of reviews
        place.reviews.append(self)
