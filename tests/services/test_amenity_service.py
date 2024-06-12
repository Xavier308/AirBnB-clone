import pytest
import uuid
from unittest.mock import MagicMock
from app.models.amenity import Amenity
from app.services.amenity_service import AmenityService
from app.persistence.data_manager import DataManager

# Fixture to mock the DataManager
@pytest.fixture
def mock_data_manager():
    mock = MagicMock(spec=DataManager)
    # Set up all methods that are used by the service
    mock.get_by_name = MagicMock()
    mock.get = MagicMock()
    mock.save = MagicMock()
    mock.update = MagicMock()
    mock.delete = MagicMock()
    mock.get_all = MagicMock()
    return mock

# Fixture for AmenityService with a mocked DataManager
@pytest.fixture
def amenity_service(mock_data_manager):
    return AmenityService(data_manager=mock_data_manager)

# Test cases
def test_create_amenity_success(amenity_service, mock_data_manager):
    mock_data_manager.get_by_name.return_value = None  # No existing amenity with the same name
    amenity_name = "Wi-Fi"
    expected_amenity = Amenity(name=amenity_name)
    
    mock_data_manager.save.return_value = expected_amenity
    result = amenity_service.create_amenity(amenity_name)
    
    assert result == expected_amenity
    mock_data_manager.save.assert_called_once_with(expected_amenity)

def test_create_amenity_failure_already_exists(amenity_service, mock_data_manager):
    amenity_name = "Wi-Fi"
    mock_data_manager.get_by_name.return_value = Amenity(name=amenity_name)  # Existing amenity
    
    with pytest.raises(ValueError, match="An amenity with this name already exists."):
        amenity_service.create_amenity(amenity_name)

def test_update_amenity_success(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    new_name = "High-Speed Internet"
    mock_amenity = Amenity(name="Wi-Fi")
    mock_data_manager.get.return_value = mock_amenity
    
    updated_amenity = amenity_service.update_amenity(amenity_id, new_name)
    
    assert updated_amenity.name == new_name
    mock_data_manager.update.assert_called_once_with(mock_amenity)

def test_update_amenity_failure_not_found(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    mock_data_manager.get.return_value = None  # Amenity not found
    
    with pytest.raises(ValueError, match="Amenity not found."):
        amenity_service.update_amenity(amenity_id, "Wi-Fi")

def test_delete_amenity_success(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    mock_amenity = Amenity(name="Wi-Fi")
    mock_data_manager.get.return_value = mock_amenity
    
    amenity_service.delete_amenity(amenity_id)
    mock_data_manager.delete.assert_called_once_with(amenity_id, Amenity)

def test_delete_amenity_failure_not_found(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    mock_data_manager.get.return_value = None  # Amenity not found
    
    with pytest.raises(ValueError, match="Amenity not found."):
        amenity_service.delete_amenity(amenity_id)

def test_get_amenity_success(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    mock_amenity = Amenity(name="Wi-Fi")
    mock_data_manager.get.return_value = mock_amenity
    
    amenity = amenity_service.get_amenity(amenity_id)
    assert amenity == mock_amenity

def test_get_amenity_failure_not_found(amenity_service, mock_data_manager):
    amenity_id = str(uuid.uuid4())
    mock_data_manager.get.return_value = None  # Amenity not found
    
    with pytest.raises(ValueError, match="Amenity not found."):
        amenity_service.get_amenity(amenity_id)

def test_get_all_amenities(amenity_service, mock_data_manager):
    mock_amenity1 = Amenity(name="Wi-Fi")
    mock_amenity2 = Amenity(name="Pool")
    mock_data_manager.get_all.return_value = [mock_amenity1, mock_amenity2]
    
    amenities = amenity_service.get_all_amenities()
    assert len(amenities) == 2
    assert mock_amenity1 in amenities
    assert mock_amenity1 in amenities and mock_amenity2 in amenities
