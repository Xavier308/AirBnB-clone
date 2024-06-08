import unittest
from app.models.city import City
from app.models.country import Country

class TestCity(unittest.TestCase):
    def setUp(self):
        self.country = Country("Utopia")
        self.city = City("Dreamtown", self.country)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Dreamtown")
        self.assertIs(self.city.country, self.country)

if __name__ == '__main__':
    unittest.main()
