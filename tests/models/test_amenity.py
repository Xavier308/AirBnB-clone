import unittest
from app.models.amenity import Amenity
from app.models.country import Country

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.country = Country("Wonderland")
        self.amenity = Amenity("Wi-Fi", self.country)

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "Wi-Fi")
        self.assertIs(self.amenity.country, self.country)

if __name__ == '__main__':
    unittest.main()
