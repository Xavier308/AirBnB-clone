import unittest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.host = User("host@example.com", "password123", "Host", "Last")
        self.place = Place(
            name="Beautiful Retreat",
            description="A quiet, cozy spot perfect for weekends.",
            address="123 Country Road",
            city="Hillsboro",
            host=self.host,
            rooms=3,
            price_per_night=150,
            max_guests=4
        )
        self.amenity = Amenity("Wi-Fi", "Global")
        self.review = Review(self.host, self.place, "Loved it!", 5)

    def test_place_creation(self):
        self.assertEqual(self.place.name, "Beautiful Retreat")
        self.assertEqual(self.place.rooms, 3)

    def test_add_amenity(self):
        self.place.add_amenity(self.amenity)
        self.assertIn(self.amenity, self.place.amenities)

    def test_add_review(self):
        self.place.add_review(self.review)
        self.assertIn(self.review, self.place.reviews)

if __name__ == '__main__':
    unittest.main()
