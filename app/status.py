from flask import Blueprint, jsonify
from flask_restx import Api, Resource
from .gpio.dfrobot_analog import read_analog_from_dfrobot
from .gpio.dfrobot_digital import read_digital_pin
from .gpio.dfrobot_pwm import get_pwm_duty_cycle
from .gpio.mcp3008 import read_analog_from_mcp3008

status_bp = Blueprint('status', __name__)
api = Api(status_bp, doc='/doc/status', title='GPIO Status API', description='API for getting the status of GPIO pins on a Raspberry Pi')

@api.route('/status')
class Status(Resource):
    @api.doc(description='Get the status of all GPIO pins.')
    def get(self):
        status = {
            'digital': [],
            'analog': [],
            'mcp3008': [],
            'pwm': []
        }

        # Read digital pins
        for pin in range(0, 28):  # Assuming digital pins are from 0 to 27
            try:
                value = read_digital_pin(pin)
                status['digital'].append({'pin': pin, 'value': value})
            except Exception:
                status['digital'].append({'pin': pin, 'value': 'Error'})

        # Read analog pins
        for pin in range(1, 5):  # Assuming analog pins are from 1 to 4
            try:
                value = read_analog_from_dfrobot(pin)
                status['analog'].append({'pin': pin, 'value': value, 'bits': 12})
            except Exception:
                status['analog'].append({'pin': pin, 'value': 'Error', 'bits': 12})

        # Read MCP3008 pins
        for pin in range(0, 8):  # Assuming MCP3008 pins are from 0 to 7
            try:
                value = read_analog_from_mcp3008(pin)
                status['mcp3008'].append({'pin': pin, 'value': value, 'bits': 10})
            except Exception:
                status['mcp3008'].append({'pin': pin, 'value': 'Error', 'bits': 10})

        # Read PWM pins
        for pin in range(1, 5):  # Assuming PWM pins are from 1 to 4
            try:
                value = get_pwm_duty_cycle(pin)
                status['pwm'].append({'pin': pin, 'value': value})
            except Exception:
                status['pwm'].append({'pin': pin, 'value': 'Error'})

        return jsonify(status)
