from flask_restx import Namespace, Resource
from app.services.user_service import UserService
from app.persistence.data_manager import DataManager
from email_validator import validate_email, EmailNotValidError

"""This user routes passed 9/9 tests"""

api = Namespace('users', description='User operations')
user_service = UserService(DataManager())


# This route was refactored to be more robust 6/13/2024
@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    def get(self):
        """List all users"""
        users = user_service.get_all_users()
        return [user.to_dict() for user in users], 200

    @api.doc('create_user')
    def post(self):
        """Create a new user"""
        data = api.payload
        required_fields = ['email', 'first_name', 'last_name', 'password']  # Include 'password' in the required fields
        if not all(field in data for field in required_fields):
            return {"error": "Missing required field"}, 400

        try:
            # Now include 'password' when calling create_user
            user = user_service.create_user(data['email'], data['first_name'], data['last_name'], data['password'])
            return user.to_dict(), 201
        except EmailNotValidError as e:
            return {"error": str(e)}, 400
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route('/<user_id>')
@api.param('user_id', 'The user identifier')
class User(Resource):
    @api.doc('get_user')
    def get(self, user_id):
        """Fetch a user given its identifier"""
        try:
            user = user_service.get_user(user_id)
            return user.to_dict(), 200
        except ValueError as e:
            return {"error": str(e)}, 404

    @api.doc('update_user')
    def put(self, user_id):
        """Update a user given its identifier"""
        data = api.payload
        try:
            user = user_service.update_user(user_id, **data)
            return user.to_dict(), 200
        except ValueError as e:
            return {"error": str(e)}, 404

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user given its identifier"""
        try:
            user_service.delete_user(user_id)
            return '', 204
        except ValueError as e:
            return {"error": str(e)}, 404
