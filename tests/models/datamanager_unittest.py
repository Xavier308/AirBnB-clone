import unittest
from app.models.user import User
from app.models.place import Place
from app.persistence.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.user = User("test@example.com", "password", "Test", "User")
        self.place = Place("Test Place", "A place", "123 Test St", "Testville", self.user, 2, 100, 2)
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)

    def test_get_user(self):
        user = self.data_manager.get(self.user.id, "User")
        self.assertEqual(user.email, "test@example.com")

    def test_update_user(self):
        user = self.data_manager.get(self.user.id, "User")
        user.email = "new@example.com"
        self.data_manager.update(user)
        updated_user = self.data_manager.get(user.id, "User")
        self.assertEqual(updated_user.email, "new@example.com")

    def test_delete_user(self):
        self.data_manager.delete(self.user.id, "User")
        user = self.data_manager.get(self.user.id, "User")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
