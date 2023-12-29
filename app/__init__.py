from flask import Flask
from .api import api_bp

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix='/api')

    # Other initialization code can be added here...

    return app
