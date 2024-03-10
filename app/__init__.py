from flask import Flask
from .api import apis_bp

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.register_blueprint(apis_bp, url_prefix='/api')

    return app
