from flask import Blueprint, jsonify, current_app, request
from .heating import target_temperature, current_temperature

# Create a Blueprint for the API routes
api_bp = Blueprint('api', __name__)

# Define a route for '/api/data' that handles GET requests
@api_bp.route('/hello', methods=['GET'])
def get_data():
    # Access the 'SECRET_KEY' configuration value from the current application
    secret_key = current_app.config['SECRET_KEY']

    # Example: Using the retrieved configuration value
    data = {'message': f'Hello, this is your data! SECRET_KEY: {secret_key}'}

    # Return the data as a JSON response
    return jsonify(data)

@api_bp.route('/current_temperature', methods=['GET'])
def get_current_temperature():
    return jsonify({'current_temperature': current_temperature})

@api_bp.route('/target_temperature', methods=['POST'])
def set_target_temperature():
    data = request.get_json()
    global target_temperature
    target_temperature = data['target_temperature']
    return jsonify({'message': f'Target temperature set to {target_temperature}°C'})
