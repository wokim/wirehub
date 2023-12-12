from flask import Flask

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Load configuration from the 'Config' class in the 'config' module
    app.config.from_object('config.Config')

    # Other initialization code can be added here...

    return app
