import unittest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User("example@example.com", "password123", "John", "Doe")
        self.place = Place("Lovely Spot", "A nice place to stay", "123 Main St", "Anytown", self.user, 3, 100, 2)
        self.review = Review(self.user, self.place, "Great place!", 5)

    def test_review_creation(self):
        self.assertEqual(self.review.text, "Great place!")
        self.assertEqual(self.review.rating, 5)

    def test_review_relationships(self):
        self.assertIn(self.review, self.place.reviews)

if __name__ == '__main__':
    unittest.main()
