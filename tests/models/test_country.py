import unittest
from app.models.country import Country
from app.models.city import City

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Narnia")
        self.city = City("Aslan's Court", self.country)

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Narnia")

    def test_add_city(self):
        self.country.add_city(self.city)  # Assuming there's an add_city method
        self.assertIn(self.city, self.country.cities)  # Assuming cities is a list in Country

if __name__ == '__main__':
    unittest.main()
