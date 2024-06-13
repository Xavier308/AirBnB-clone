from flask_testing import TestCase
from app.app import create_app  # Ensure correct import based on your project structure
from unittest.mock import patch, MagicMock
# import warnings

# Assuming User class has methods like to_dict() needed for these tests
from app.models.user import User  # Import your User model if it's lightweight and doesn't need database interaction


# The test throw some warnings but it works fine
class MockUser:
    def __init__(self, user_id, email, first_name, last_name):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

class TestUserAPI(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.storage = MagicMock()
        # Instead of dictionaries, return MockUser instances or real User instances
        self.mock_data_manager.storage.values.return_value = [
            MockUser('1', 'test@example.com', 'John', 'Doe')
        ]
        self.patcher = patch('app.api.user_routes.user_service.data_manager', self.mock_data_manager)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    # This test pass
    def test_user_list(self):
        response = self.client.get('/users/')
        self.assert200(response)
        # Add assertions to verify the structure and content of the response
        data = response.json
        self.assertEqual(data[0]['email'], 'test@example.com')

    # This test pass**
    def test_create_user_success(self):
        # Mock the user_service.create_user method to return a user
        with patch('app.api.user_routes.user_service.create_user') as mock_create_user:
            mock_create_user.return_value = MockUser('2', 'new@example.com', 'Alice', 'Wonderland')
            response = self.client.post('/users/', json={
                'email': 'new@example.com', 'first_name': 'Alice', 'last_name': 'Wonderland'
            })
            self.assertStatus(response, 201)

    # This test pass
    def test_create_user_failure(self):
        # Simulate failure (e.g., missing field)
        response = self.client.post('/users/', json={
            'email': 'new@example.com', 'first_name': 'Alice'  # Missing last_name
        })
        self.assertStatus(response, 400)

    # This test pass
    def test_get_user_success(self):
        # Mock the user_service.get_user method to return a user
        with patch('app.api.user_routes.user_service.get_user') as mock_get_user:
            mock_get_user.return_value = MockUser('1', 'test@example.com', 'John', 'Doe')
            response = self.client.get('/users/1')
            self.assert200(response)
            self.assertEqual(response.json['email'], 'test@example.com')

    # This test pass
    def test_get_user_not_found(self):
        # Simulate user not found
        with patch('app.api.user_routes.user_service.get_user') as mock_get_user:
            mock_get_user.side_effect = ValueError("User not found")
            response = self.client.get('/users/999')
            self.assert404(response)

    # This test pass
    def test_update_user_success(self):
        # Mock the user_service.update_user method to simulate updating the user's email
        with patch('app.api.user_routes.user_service.update_user') as mock_update_user:
            mock_update_user.return_value = MockUser('1', 'updated@example.com', 'John', 'Doe')
            response = self.client.put('/users/1', json={'email': 'updated@example.com'})
            self.assert200(response)
            self.assertEqual(response.json['email'], 'updated@example.com')

    # This test pass
    def test_update_user_not_found(self):
        # Simulate user not found during update
        with patch('app.api.user_routes.user_service.update_user') as mock_update_user:
            mock_update_user.side_effect = ValueError("User not found")
            response = self.client.put('/users/999', json={'email': 'fail@example.com'})
            self.assertStatus(response, 404)
            #self.assert404(response)

    # One of the following two test failed
    def test_delete_user_success(self):
        # Mock the user_service.delete_user method to simulate successful deletion
        with patch('app.api.user_routes.user_service.delete_user') as mock_delete_user:
            mock_delete_user.return_value = None  # No return value needed for delete
            response = self.client.delete('/users/1')
            self.assertStatus(response, 204)

    def test_delete_user_not_found(self):
        # Simulate user not found during deletion
        with patch('app.api.user_routes.user_service.delete_user') as mock_delete_user:
            mock_delete_user.side_effect = ValueError("User not found")
            response = self.client.delete('/users/999')
            self.assertStatus(response, 404)
            # self.assert404(response)

# This worked fine
if __name__ == '__main__':
    import unittest
    unittest.main()
