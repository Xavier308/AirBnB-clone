import pytest
from unittest.mock import patch, MagicMock
from app.models.place import Place
from app.models.city import City
from app.models.user import User
from app.services.place_service import PlaceService
from app.persistence.data_manager import DataManager

# Fixture to mock the DataManager
@pytest.fixture
def mock_data_manager():
    return MagicMock(spec=DataManager)

# Fixture for PlaceService with a mocked DataManager
@pytest.fixture
def place_service(mock_data_manager):
    return PlaceService(data_manager=mock_data_manager)

# Tests start here
mock_city = City(name="Springfield", country="USA")
mock_user = User(email="host@example.com", first_name="Host", last_name="Example", password="secure_password")

# The two first tests are working. Ckeck the comment in the commented tests.
def test_create_place_success(place_service, mock_data_manager):
    mock_data_manager.get.return_value = mock_city  # Assume city exists
    new_place_data = {
        "name": "Lovely Stay",
        "description": "Comfortable, quiet and convenient.",
        "address": "123 Lakeview",
        "city_id": mock_city.city_id,  # Assuming City class has city_id attribute
        "latitude": 38.8977,
        "longitude": -77.0365,
        "host_id": mock_user.email,  # Assuming the host_id can be derived from User's email
        "rooms": 3,
        "bathrooms": 2,
        "price_per_night": 120,
        "max_guests": 5,
        "amenities": ["Wi-Fi", "Air Conditioning"]
    }

    # name, description, address, city_id, latitude, longitude, host_id, 
    # rooms, bathrooms, price, max_guests, amenities

    # Simulate the expected place to be created
    expected_place = Place(**new_place_data)
    mock_data_manager.save.return_value = expected_place

    # Ensure the city exists before calling create_place
    with patch.object(mock_data_manager, 'get', return_value=True):
        place = place_service.create_place(**new_place_data)

    assert place == expected_place
    mock_data_manager.save.assert_called_once_with(expected_place)

def test_create_place_failure_nonexistent_city(place_service, mock_data_manager):
    mock_data_manager.get.return_value = None  # Simulate city does not exist
    new_place_data = {
        "name": "Misty Villa",
        "description": "Hidden retreat",
        "address": "456 Foggy Lane",
        "city_id": "nonexistent_city_id",
        "latitude": 34.0522,
        "longitude": -118.2437,
        "host_id": mock_user.email,
        "rooms": 2,
        "bathrooms": 1,
        "price_per_night": 150,
        "max_guests": 4,
        "amenities": ["Garden", "Patio"]
    }

    with pytest.raises(ValueError, match="City does not exist."):
        place_service.create_place(**new_place_data)

# Other tests for the service code but its needed to implement some
# changes in the code logic. This would be worked later.
'''
def test_create_place_failure_invalid_data(place_service, mock_data_manager):
    mock_data_manager.get.return_value = mock_city  # Assume city exists
    new_place_data = {
        "name": "",
        "description": "A place with invalid data",
        "address": "",
        "city_id": mock_city.city_id,
        "latitude": 200,  # Invalid latitude
        "longitude": 200,  # Invalid longitude
        "host_id": mock_user.email,
        "rooms": -1,  # Invalid number of rooms
        "bathrooms": -1,  # Invalid number of bathrooms
        "price_per_night": -100,  # Negative price
        "max_guests": 0,  # Zero guests not logical
        "amenities": []
    }

    with pytest.raises(ValueError):
        place_service.create_place(**new_place_data)

def test_update_place_success(place_service, mock_data_manager):
    mock_place = Place(**valid_place_data)  # valid_place_data should be defined similar to new_place_data
    updated_data = {"name": "Updated Name", "price_per_night": 200}
    mock_data_manager.get.return_value = mock_place
    mock_data_manager.update.return_value = None  # Assuming update does not return a value

    # Perform the update
    updated_place = place_service.update_place(mock_place.place_id, **updated_data)
    assert updated_place.name == "Updated Name"
    assert updated_place.price_per_night == 200
    mock_data_manager.update.assert_called_once()
'''