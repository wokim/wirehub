from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource
from .gpio.dfrobot_analog import read_analog_from_dfrobot
from .gpio.dfrobot_digital import write_digital_pin, read_digital_pin
from .gpio.dfrobot_pwm import set_pwm_duty_cycle, get_pwm_duty_cycle
from .gpio.mcp3008 import read_analog_from_mcp3008

pins_bp = Blueprint('pins', __name__)
api = Api(pins_bp, doc='/doc/pins', title='GPIO Pin Control API', description='API for controlling GPIO pins on a Raspberry Pi')

@api.route('/digital/<int:pin>')
@api.doc(params={'pin': 'A GPIO pin number for digital I/O'})
class DigitalPin(Resource):
    @api.doc(description='Read the digital input value from a specified GPIO pin.')
    def get(self, pin):
        try:
            value = read_digital_pin(pin)
            return {'pin': pin, 'value': value}
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the digital pin.'}, 500

    @api.doc(description='Write a digital output value to a specified GPIO pin.')
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

@api.route('/pwm/<int:pin>')
@api.doc(params={'pin': 'A GPIO pin number for PWM output'})
class PWMPin(Resource):
    @api.doc(description='Read the PWM duty cycle value from a specified pin.')
    def get(self, pin):
        try:
            value = get_pwm_duty_cycle(pin)
            return {'pin': pin, 'value': value}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the PWM duty cycle.'}, 500

    @api.doc(description='Write a PWM duty cycle value to a specified pin.')
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

@api.route('/analog/<int:pin>')
@api.doc(params={'pin': 'A GPIO pin number for analog input'})
class AnalogPin(Resource):
    @api.doc(description='Read the analog value from a specified DFRobot Expansion Board pin.')
    def get(self, pin):
        try:
            value = read_analog_from_dfrobot(pin)
            return {'pin': pin, 'value': value, 'bits': 12}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the analog pin.'}, 500

@api.route('/mcp3008/<int:pin>')
@api.doc(params={'pin': 'A channel number on the MCP3008 ADC'})
class MCP3008Pin(Resource):
    @api.doc(description='Read the analog value from a specified MCP3008 channel.')
    def get(self, pin):
        try:
            value = read_analog_from_mcp3008(pin)
            return {'pin': pin, 'value': value, 'bits': 10}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'An error occurred while reading the MCP3008 analog pin.'}, 500
