from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, title='AirBnB SuperClone', version='6.9', description='The Best API in the World')

    # Configuration settings might be loaded here
    app.config.from_pyfile('config.py')

    # Absolute imports
    from app.api.user_routes import api as users_ns
    from app.api.place_routes import api as places_ns
    from app.api.location_routes import api as locations_ns
    from app.api.amenity_routes import api as amenities_ns
    from app.api.review_routes import api as reviews_ns

    api.add_namespace(users_ns)
    api.add_namespace(places_ns)
    api.add_namespace(locations_ns)
    api.add_namespace(amenities_ns)
    api.add_namespace(reviews_ns)

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True, host='0.0.0.0')
