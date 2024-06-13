from flask_testing import TestCase
from app.app import create_app  # Ensure correct import based on your project structure
from unittest.mock import patch, MagicMock

# Assuming Place class has methods like to_dict() needed for these tests
from app.models.place import Place  # Import your Place model

class MockPlace:
    def __init__(self, place_id, name, description, address, city_id, latitude, longitude, host_id, rooms, bathrooms, price_per_night, max_guests, amenities):
        self.place_id = place_id
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities

    def to_dict(self):
        return {
            'place_id': self.place_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'rooms': self.rooms,
            'bathrooms': self.bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': self.amenities
        }

class TestPlaceAPI(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.storage = MagicMock()
        self.mock_data_manager.storage.values.return_value = [
            MockPlace('1', 'Lakeside Cottage', 'A beautiful spot by the lake', '123 Lake Road', '1', 45.4215, -75.6919, '100', 3, 2, 200, 6, ['Wi-Fi', 'Parking'])
        ]
        self.patcher = patch('app.api.place_routes.place_service.data_manager', self.mock_data_manager)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_place_list(self):
        response = self.client.get('/places/')
        self.assert200(response)
        data = response.json
        self.assertEqual(data[0]['name'], 'Lakeside Cottage')

    def test_create_place_success(self):
        with patch('app.api.place_routes.place_service.create_place') as mock_create_place:
            mock_create_place.return_value = MockPlace('2', 'Mountain Retreat', 'Escape in the mountains', '456 Mountain Road', '2', 40.7128, -74.0060, '101', 5, 3, 300, 8, ['Fireplace', 'Mountain View'])
            response = self.client.post('/places/', json={
                'name': 'Mountain Retreat', 
                'description': 'Escape in the mountains',
                'address': '456 Mountain Road',
                'city_id': '2',
                'latitude': 40.7128,
                'longitude': -74.0060,
                'host_id': '101',
                'rooms': 5,
                'bathrooms': 3,
                'price_per_night': 300,
                'max_guests': 8,
                'amenities': ['Fireplace', 'Mountain View']
            })
            self.assertStatus(response, 201)

    def test_create_place_failure(self):
        response = self.client.post('/places/', json={
            'name': 'Incomplete Place'  # Missing many required fields
        })
        self.assert400(response)

if __name__ == '__main__':
    import unittest
    unittest.main()
