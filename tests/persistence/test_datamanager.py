import pytest
import json
import tempfile
from app.persistence.data_manager import DataManager


class User:
    def __init__(self, user_id, email):
        self.id = user_id
        self.email = email

    def to_dict(self):
        return {
            'user_id': self.id,  # Ensure the key matches the constructor argument name
            'email': self.email
        }

@pytest.fixture
def user():
    return User(user_id="1", email="user@example.com")

@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        yield tmpfile.name  # Provide the filename to use in the test

@pytest.fixture
def data_manager(temp_file):
    """Fixture to create a DataManager instance with a temporary file."""
    return DataManager(filename=temp_file)

def test_data_manager_initialization(data_manager):
    assert isinstance(data_manager.load_data(), dict), "Should load data as a dictionary"

# Assuming that you're updating the User constructor and its uses accordingly:
def test_save_and_get_entity(data_manager, temp_file):
    user = User(user_id="1", email='test@example.com')
    data_manager.save(user)
    # Ensure data is saved to file
    with open(temp_file, 'r') as file:
        data = json.load(file)
    assert str(user.id) in data['User'], "User should be saved in the file under its ID"
    
    retrieved_user = data_manager.get(user.id, User)
    assert retrieved_user.email == user.email, "Should retrieve the user with correct email"

def test_update_entity(data_manager):
    user = User(user_id="1", email='original@example.com')
    data_manager.save(user)
    user.email = 'updated@example.com'
    data_manager.update(user)
    
    updated_user = data_manager.get(user.id, User)
    assert updated_user.email == 'updated@example.com', "Email should be updated in the storage"

def test_delete_entity(data_manager):
    user = User(user_id=1, email='test@example.com')
    data_manager.save(user)
    data_manager.delete(user.id, User)
    
    assert data_manager.get(user.id, User) is None, "Deleted user should not be retrievable"

# Additional test for file-based scenario
def test_non_existent_file_load():
    manager = DataManager(filename='nonexistent.json')
    assert manager.load_data() == {}, "Should return an empty dictionary for a nonexistent file"
