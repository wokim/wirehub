from flask import Flask
from .pins import pins_bp
from .status import status_bp

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.register_blueprint(pins_bp, url_prefix='/api')
    app.register_blueprint(status_bp, url_prefix='/api')

    return app
