import unittest
from app.models.user import User
from app.models.place import Place

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("example@example.com", "password123", "John", "Doe")
        self.assertEqual(user.email, "example@example.com")

    def test_add_place(self):
        user = User("example@example.com", "password123", "John", "Doe")
        place = Place("Lovely Spot", "A nice place to stay", "123 Main St", "Anytown", user, 3, 100, 2)
        user.add_place(place)
        self.assertIn(place, user.places)

if __name__ == '__main__':
    unittest.main()
