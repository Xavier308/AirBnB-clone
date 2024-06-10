# It is essential to patch first and the use MagicMock
from unittest.mock import patch, MagicMock
import pytest
from app.models.user import User
from app.services.user_service import UserService
from app.persistence.data_manager import DataManager

'''
This file is working properly.
It do 4 test
'''


@pytest.fixture
def mock_data_manager():
    return MagicMock(spec=DataManager)

@pytest.fixture
def user_service(mock_data_manager):
    return UserService(data_manager=mock_data_manager)

def test_create_user_failure_due_to_existing_email(user_service, mock_data_manager):
    mock_data_manager.get.return_value = User(email="test@example.com", first_name="John", last_name="Doe", password="secret")
    with patch('app.services.user_service.validate_email'), \
         pytest.raises(ValueError, match="Email already in use"):
        user_service.create_user("test@example.com", "John", "Doe", "secret")

def test_get_user_not_found(user_service, mock_data_manager):
    mock_data_manager.get.return_value = None  # No user found
    with pytest.raises(ValueError, match="User not found"):
        user_service.get_user(1)

def test_update_user(user_service, mock_data_manager):
    mock_user = User(email="old@example.com", first_name="John", last_name="Doe", password="secret")
    mock_data_manager.get.return_value = mock_user
    updated_user = user_service.update_user(1, email="new@example.com")
    assert updated_user.email == "new@example.com"
    mock_data_manager.update.assert_called_once()

def test_delete_user(user_service, mock_data_manager):
    mock_user = User(email="test@example.com", first_name="John", last_name="Doe", password="secret")
    mock_data_manager.get.return_value = mock_user
    user_service.delete_user(1)
    mock_data_manager.delete.assert_called_with(1, User)
