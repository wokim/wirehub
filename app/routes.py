from flask import Blueprint, jsonify, current_app

# Create a Blueprint for the API routes
api_bp = Blueprint('api', __name__)

# Define a route for '/api/data' that handles GET requests
@api_bp.route('/api/data', methods=['GET'])
def get_data():
    # Access the 'SECRET_KEY' configuration value from the current application
    secret_key = current_app.config['SECRET_KEY']

    # Example: Using the retrieved configuration value
    data = {'message': f'Hello, this is your data! SECRET_KEY: {secret_key}'}

    # Return the data as a JSON response
    return jsonify(data)
