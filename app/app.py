from flask import Flask
from app.api import user_routes, place_routes

def create_app():
    app = Flask(__name__)
    
    # Configuration settings might be loaded here
    app.config.from_pyfile('config.py')

    # Registering blueprints from the api package
    app.register_blueprint(user_routes.blueprint)
    app.register_blueprint(place_routes.blueprint)
    
    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True, host='0.0.0.0')
