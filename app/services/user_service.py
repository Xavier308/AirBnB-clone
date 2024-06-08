from app.models.user import User
from app.persistence.data_manager import DataManager
from email_validator import validate_email, EmailNotValidError

class UserService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def create_user(self, email, first_name, last_name):
        # Validate email format
        validate_email(email)

        # Ensure email is unique
        if self.data_manager.get(email, User):
            raise ValueError("Email already in use")

        # Validate non-empty first and last name
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty")

        # Create and save the new user
        new_user = User(email=email, first_name=first_name, last_name=last_name)
        self.data_manager.save(new_user)
        return new_user

    def get_user(self, user_id):
        user = self.data_manager.get(user_id, User)
        if not user:
            raise ValueError("User not found")
        return user

    def update_user(self, user_id, email=None, first_name=None, last_name=None):
        user = self.get_user(user_id)
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        self.data_manager.update(user)
        return user

    def delete_user(self, user_id):
        self.get_user(user_id)  # Ensure user exists before attempting to delete
        self.data_manager.delete(user_id, User)
