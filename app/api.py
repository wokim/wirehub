from flask import Blueprint, request, jsonify
from .gpio.analog_ports import read_analog
from .gpio.digital_ports import set_digital_output, get_digital_input
from .gpio.pwm_ports import set_pwm_duty, get_pwm_duty
from .gpio import board
from .gpio.mcp3008 import read_adc

# Create a Blueprint for the api routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/adc/<int:pin>', methods=['GET'])
def read_analog_data(pin):
    try:
        if 0 <= pin <= 3:
            value = read_analog(pin+1)
            return jsonify({'pin': pin, 'value': value, 'bits': 12})
        else:
            return jsonify({'error': 'Invalid pin number. Should be between 0 and 3.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin number. Should be an integer.'}), 400

@api_bp.route('/mcp3008/<int:pin>', methods=['GET'])
def read_mcp3008_data(pin):
    try:
        if 0 <= pin <= 7:
            value = read_adc(pin)
            return jsonify({'pin': pin, 'value': value, 'bits': 10})
        else:
            return jsonify({'error': 'Invalid pin number. Should be between 0 and 7.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin number. Should be an integer.'}), 400

@api_bp.route('/digital/<int:pin>', methods=['GET'])
def read_digital_data(pin):
    try:
        if 22 <= pin <= 27:
            value = get_digital_input(pin)
            return jsonify({'pin': pin, 'value': value == 1})
        else:
            return jsonify({'error': 'Invalid pin number. Should be between 22 and 27.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin number. Should be an integer.'}), 400

@api_bp.route('/digital', methods=['PUT'])
def write_digital_data():
    try:
        data = request.json

        pin = data.get('pin')
        value = data.get('value')

        if isinstance(pin, int) and 22 <= pin <= 27 and isinstance(value, bool):
            set_digital_output(pin, value)
            return jsonify({'pin': pin, 'value': value})
        else:
            return jsonify({'error': 'Invalid pin or value. Pin should be an integer between 22 and 27, and value should be a boolean (True or False).'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin or value. Pin should be an integer, and value should be a boolean (True or False).'}), 400

@api_bp.route('/pwm_duty/<int:pin>', methods=['GET'])
def read_pwm_duty(pin):
    try:
        if 0 <= pin <= 3:
            value = get_pwm_duty(pin+1)
            return jsonify({'pin': pin, 'value': value})
        else:
            return jsonify({'error': 'Invalid pin number. Should be between 0 and 3.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin number. Should be an integer.'}), 400

@api_bp.route('/pwm_duty', methods=['PUT'])
def write_pwm_duty():
    try:
        data = request.json

        pin = data.get('pin')
        value = data.get('value')

        if isinstance(pin, int) and 0 <= pin <= 3 and isinstance(value, (int, float)) and 0.0 <= value <= 100.0:
            set_pwm_duty(pin+1, value)
            return jsonify({'pin': pin, 'value': value})
        else:
            return jsonify({'error': 'Invalid pin or value. Pin should be an integer between 0 and 3, and value should be a float between 0.0 and 100.0.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid pin or value. Pin should be an integer, and value should be a float.'}), 400

@api_bp.route('/info', methods=['GET'])
def read_info():
    ret = {
        'pwm': [],
        'analog': [],
        'mcp3008': [],
        'digital': [],
        'bits': {'mcp3008': 10, 'analog': 12}
    }
    for i in range(0, 4):
        ret['pwm'].append(get_pwm_duty(i+1))
        ret['analog'].append(read_analog(i+1))
    for j in range(0, 8):
        ret['mcp3008'].append(read_adc(j))
    for k in range(22, 28):
        ret['digital'].append(get_digital_input(k) == 1)

    return jsonify(ret)
