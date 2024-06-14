from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, title='AirBnB SuperClone', version='3.3', description='The Best API in the World')
    # api = Api(app, title='AirBnB SuperClone', version='3.3', description='The Best API in the World', doc=False)

    # Configuration settings might be loaded here
    app.config.from_pyfile('config.py')

    # Absolute imports
    from app.api.user_routes import api as users_ns
    from app.api.place_routes import api as places_ns
    from app.api.city_routes import api as city_ns
    from app.api.country_routes import api as country_ns
    from app.api.amenity_routes import api as amenities_ns
    from app.api.review_routes import api as reviews_ns

    api.add_namespace(users_ns)
    api.add_namespace(places_ns)
    api.add_namespace(city_ns)
    api.add_namespace(country_ns)
    api.add_namespace(amenities_ns)
    api.add_namespace(reviews_ns)

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True, host='0.0.0.0')
