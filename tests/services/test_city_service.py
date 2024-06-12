import pytest
from unittest.mock import MagicMock
from app.models.city import City
from app.models.user import User
from app.services.city_service import CityService
from app.persistence.data_manager import DataManager


# Fixture to mock the DataManager
@pytest.fixture
def mock_data_manager():
    mock = MagicMock(spec=DataManager)
    mock.get_all = MagicMock()  # Add this line to explicitly set up the get_all method
    return mock

# Fixture for CityService with a mocked DataManager
@pytest.fixture
def city_service(mock_data_manager):
    return CityService(data_manager=mock_data_manager)

mock_city = City(name="Springfield", country="USA")  # Corrected country parameter
mock_user = User(email="host@example.com", first_name="Host", last_name="Example", password="secure_password")

def test_create_city_success(city_service, mock_data_manager):
    mock_data_manager.get.return_value = None  # No city with this name and country code exists
    new_city_data = {
        "name": "Springfield",
        "country": "USA"  # Corrected from country_code to country
    }

    expected_city = City(**new_city_data)
    mock_data_manager.save.return_value = expected_city

    city = city_service.create_city(name="Springfield", country="USA")

    assert city == expected_city
    mock_data_manager.save.assert_called_once_with(expected_city)

# Other tests...

def test_create_city_failure_already_exists(city_service, mock_data_manager):
    # Setup the DataManager mock to return a city indicating it already exists
    mock_data_manager.get.return_value = mock_city
    with pytest.raises(ValueError, match="City with this name already exists in the specified country."):
        city_service.create_city(name="Springfield", country="USA")


def test_update_city_success(city_service, mock_data_manager):
    updated_name = "New Springfield"
    # Setup the DataManager mock to return the city initially, then test updating it
    mock_data_manager.get.return_value = mock_city
    city_service.update_city(city_id=mock_city.city_id, name=updated_name)

    # Check that the name was updated in the mock object
    assert mock_city.name == updated_name
    mock_data_manager.update.assert_called_once_with(mock_city)

def test_delete_city_success(city_service, mock_data_manager):
    # Setup the DataManager mock to return the city, indicating it exists for deletion
    mock_data_manager.get.return_value = mock_city
    city_service.delete_city(city_id=mock_city.city_id)

    # Check that delete was called on the DataManager
    mock_data_manager.delete.assert_called_once_with(mock_city.city_id, City)


def test_get_all_cities(city_service, mock_data_manager):
    # Setup the DataManager mock to return a list of cities
    mock_data_manager.get_all.return_value = [mock_city, City(name="Shelbyville", country="USA")]
    cities = city_service.get_all_cities()

    # Check the count and presence of mock_city
    assert len(cities) == 2
    assert mock_city in cities  # This checks object presence which requires a correct setup in City.__eq__
