from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields, Namespace
from .gpio.dfrobot_analog import read_analog_from_dfrobot
from .gpio.dfrobot_digital import write_digital_pin, read_digital_pin
from .gpio.dfrobot_pwm import set_pwm_duty_cycle, get_pwm_duty_cycle
from .gpio.mcp3008 import read_analog_from_mcp3008

# Creating a Flask Blueprint
api_bp = Blueprint('api', __name__)
api = Api(api_bp, doc='/doc/', title='WireHub API', description='A Flask Restx powered API for controlling GPIOs on Raspberry Pi')

# Defining a Flask-RESTx Namespace
ns = Namespace('gpio', description='GPIO control and status endpoints')

# Adding the Namespace to the Api object
api.add_namespace(ns)

# Model for digital pin
digital_pin_model = ns.model('DigitalPinModel', {
    'value': fields.Boolean(required=True, description='The digital value to set on the GPIO pin (True for HIGH, False for LOW)')
})

# Model for PWM pin
pwm_pin_model = ns.model('PWMPinModel', {
    'value': fields.Float(required=True, min=0.0, max=100.0, description='The PWM duty cycle value (0.0 to 100.0)')
})

# Endpoint for digital pin
@ns.route('/digital/<int:pin>')
@ns.doc(params={'pin': 'A GPIO pin number for digital I/O'})
class DigitalPin(Resource):
    @ns.doc(description='Read the digital input value from a specified GPIO pin.')
    def get(self, pin):
        try:
            value = read_digital_pin(pin)
            return {'pin': pin, 'value': value}
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the digital pin.'}, 500

    @ns.doc(description='Write a digital output value to a specified GPIO pin.')
    @ns.expect(digital_pin_model)
    def put(self, pin):
        data = request.get_json()
        value = data.get('value', None)
        try:
            write_digital_pin(pin, value)
            return {'pin': pin, 'value': value}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while writing to the digital pin.'}, 500

# Endpoint for PWM pin
@ns.route('/pwm/<int:pin>')
@ns.doc(params={'pin': 'A GPIO pin number for PWM output'})
class PWMPin(Resource):
    @ns.doc(description='Read the PWM duty cycle value from a specified pin.')
    def get(self, pin):
        try:
            value = get_pwm_duty_cycle(pin)
            return {'pin': pin, 'value': value}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the PWM duty cycle.'}, 500

    @ns.doc(description='Write a PWM duty cycle value to a specified pin.')
    @ns.expect(pwm_pin_model)
    def put(self, pin):
        data = request.get_json()
        value = data.get('value', None)
        try:
            set_pwm_duty_cycle(pin, value)
            return {'pin': pin, 'value': value}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while setting the PWM duty cycle.'}, 500

@ns.route('/analog/<int:pin>')
@ns.doc(params={'pin': 'A GPIO pin number for analog input'})
class AnalogPin(Resource):
    @ns.doc(description='Read the analog value from a specified DFRobot Expansion Board pin.')
    def get(self, pin):
        try:
            value = read_analog_from_dfrobot(pin)
            return {'pin': pin, 'value': value, 'bits': 12}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the analog pin.'}, 500

@ns.route('/mcp3008/<int:pin>')
@ns.doc(params={'pin': 'A channel number on the MCP3008 ADC'})
class MCP3008Pin(Resource):
    @ns.doc(description='Read the analog value from a specified MCP3008 channel.')
    def get(self, pin):
        try:
            value = read_analog_from_mcp3008(pin)
            return {'pin': pin, 'value': value, 'bits': 10}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the MCP3008 analog pin.'}, 500

# Endpoint for status
@ns.route('/status')
class Status(Resource):
    @ns.doc(description='Get the status of all GPIO pins.')
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
