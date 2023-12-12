from flask import Blueprint, jsonify
from .gpio.analog_ports import read_analog
from .gpio.digital_ports import set_digital_output
from .gpio.pwm_ports import set_pwm_duty
from .gpio import board
import math

# Create a Blueprint for the test routes
test_bp = Blueprint('test', __name__)

@test_bp.route('/read_analog', methods=['GET'])
def read_analog_data():
    val = read_analog(board.A0)
    data = {'value': f'{val}'}
    return jsonify(data)

@test_bp.route('/read_temperature', methods=['GET'])
def read_temperature():
    val = read_analog(board.A0)
    Vin = 3.3
    R1 = 10000 # 브레드보드의 저항
    RT0 = 10000 # 기준온도 (섭씨 25도)에서의 온도계의 저항
    T0 = 25 + 273.15 # 온도계 기준온도 (절대온도)
    B = 3950

    # Conversion to voltage
    Vout = Vin * (val / 4095)
    # Resistance of RT
    RT = (-1.0 * R1 * Vout) / (Vout - Vin)

    # Steinhart-Hart equation
    ln = math.log(RT / RT0)
    temp_k = (1 / (ln / B + 1 / T0))
    temp = temp_k - 273.15

    return jsonify({'temperature': f'{temp}'})

@test_bp.route('/digital_high', methods=['GET'])
def set_digital_high():
    set_digital_output(0, True)
    return jsonify({"0": True})

@test_bp.route('/digital_low', methods=['GET'])
def set_digital_low():
    set_digital_output(0, False)
    return jsonify({"0": False})

@test_bp.route('/pwm_duty_none', methods=['GET'])
def set_pwm_duty_none():
    set_pwm_duty(0, 0)
    return jsonify({"0": 0})

@test_bp.route('/pwm_duty_half', methods=['GET'])
def set_pwm_duty_half():
    set_pwm_duty(0, 50)
    return jsonify({"0": 50})

@test_bp.route('/pwm_duty_full', methods=['GET'])
def set_pwm_duty_full():
    set_pwm_duty(0, 100)
    return jsonify({"0": 100})
