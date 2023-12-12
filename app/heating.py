import requests
from .gpio.pid_controller import PIDController
from .gpio.pwm_ports import set_pwm_duty

current_temperature = None  # 초기값은 None으로 설정
target_temperature = None
pid_controller = None

def pid_output_to_pwm_duty_cycle(pid_output, max_pwm_value=100):
    """
    Convert PID control output to PWM duty cycle.

    Parameters:
    - pid_output (float): PID control output
    - max_pwm_value (float): Maximum PWM duty cycle value (default is 100)

    Returns:
    - float: PWM duty cycle value
    """

    # 현재온도 18도, 타겟온도 25도일떄 pid_output: 7.77
    # 현재온도 22도, 타겟온도 25도일 때 3.32
    # 현재온도 24도, 타겟온도 25도 일 때 pid_output 1.11

    pwm_duty_cycle = pid_output * 100
    return max(0, min(max_pwm_value, pwm_duty_cycle))  # Ensure the result is within the valid range (0 to max_pwm_value)

def get_current_temperature():
    try:
        # 외부 서비스에서 현재 온도 가져오기
        response = requests.get('http://external:5000/api/current_temperature')
        data = response.json()
        return data['current_temperature']
    except Exception as e:
        print(f"Error fetching external temperature: {e}")
        # return None
        return 23 # HACK

def check_temperature():
    global pid_controller, target_temperature

    if target_temperature is None:
        return

    if pid_controller is None:
        pid_controller = PIDController(kp=1.0, ki=0.1, kd=0.01, setpoint=target_temperature)

    global current_temperature
    current_temp = get_current_temperature()
    if current_temp is not None:
        current_temperature = current_temp
        control_output = pid_controller.calculate_output(current_temperature)
        converted_pwm_duty_cycle = pid_output_to_pwm_duty_cycle(control_output)
        set_pwm_duty(0, converted_pwm_duty_cycle)
        print(f"Current Temperature: {current_temperature}°C, Target Temperature: {target_temperature} PWM Output: {converted_pwm_duty_cycle}")