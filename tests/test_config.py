import unittest
from app import create_app
from app.config import TestingConfig

class TestDevelopmentConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['SECRET_KEY'] is 'your_secret_key')
        self.assertTrue(self.app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///testing.db')

if __name__ == '__main__':
    unittest.main()
