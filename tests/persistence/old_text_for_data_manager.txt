import pytest
from app.persistence.data_manager import DataManager  # Adjust the import according to your project structure

'''
This code passed 5 test:
1- Initializing its storage dictionary.
2 -Saving entities based on their type and ID.
3- It is accurately retrieving entities when they exist and correctly returning None when they don't.
4- It successfully updates existing entities and retains the changes.
5- It properly deletes entities from the storage and ensures they cannot be retrieved afterwards.

Additional test to consider:
attempt to update or delete an entity that does not exist

'''


# Assuming a simple User class for testing purposes
class User:
    def __init__(self, user_id, email):
        self.id = user_id
        self.email = email

@pytest.fixture
def data_manager():
    """Fixture to create a DataManager instance for each test."""
    return DataManager()

def test_data_manager_initialization(data_manager):
    assert isinstance(data_manager.storage, dict), "Storage should be initialized as a dictionary"
    assert data_manager.storage == {}, "Storage should be empty on initialization"

def test_save_entity(data_manager):
    user = User(user_id=1, email='test@example.com')
    data_manager.save(user)
    assert 'User' in data_manager.storage, "User type should be a key in the storage dictionary"
    assert data_manager.storage['User'][1] == user, "User should be saved under its ID"

def test_get_entity(data_manager):
    user = User(user_id=1, email='test@example.com')
    data_manager.save(user)
    retrieved_user = data_manager.get(1, 'User')
    assert retrieved_user == user, "Should retrieve the correct user"
    assert data_manager.get(2, 'User') is None, "Should return None for a non-existent ID"
    assert data_manager.get(1, 'NonExistentType') is None, "Should return None for a non-existent type"

def test_update_entity(data_manager):
    user = User(user_id=1, email='original@example.com')
    data_manager.save(user)
    updated_user = User(user_id=1, email='updated@example.com')
    data_manager.update(updated_user)
    assert data_manager.storage['User'][1].email == 'updated@example.com', "Email should be updated in storage"

def test_delete_entity(data_manager):
    user = User(user_id=1, email='test@example.com')
    data_manager.save(user)
    data_manager.delete(1, 'User')
    assert 1 not in data_manager.storage['User'], "User should be deleted from storage"
    assert data_manager.get(1, 'User') is None, "Deleted user should not be retrievable"
