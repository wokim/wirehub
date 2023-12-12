from flask import Flask
from .api import api_bp
from .test import test_bp

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Load configuration from the 'Config' class in the 'config' module
    app.config.from_object('config.Config')

    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(test_bp, url_prefix='/test')

    # Other initialization code can be added here...

    return app
