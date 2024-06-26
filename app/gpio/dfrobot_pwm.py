from . import board

def set_pwm_duty_cycle(channel, duty_cycle):
    """
    Set the PWM duty cycle for a specified channel on the DFRobot Expansion Board.

    The DFRobot Expansion Board provides four groups of PWM ports, which can be controlled
    via I2C communication from the Raspberry Pi to the on-board STM32 microcontroller.
    The VP port can supply 6-12V external power to the PWM port. When not powered, the
    voltage of PWM ⊕ is 3.3V.

    Args:
        channel (int): The PWM channel to set (0-3).
        duty_cycle (float): The duty cycle to set for the channel (0.0 - 100.0).

    Raises:
        ValueError: If the specified channel or duty cycle is out of range.
    """
    if not 0 <= channel <= 3:
        raise ValueError("Channel must be an integer between 0 and 3")
    if not 0.0 <= duty_cycle <= 100.0:
        raise ValueError("Duty cycle must be a float between 0.0 and 100.0")

    # DFRobot Expansion Board index is 1-based
    board.set_pwm_duty(channel + 1, duty_cycle)

def get_pwm_duty_cycle(channel):
    """
    Get the current PWM duty cycle for a specified channel on the DFRobot Expansion Board.

    Args:
        channel (int): The PWM channel to get (0-3).

    Returns:
        float: The current duty cycle for the specified channel.

    Raises:
        ValueError: If the specified channel is out of range.
    """
    if not 0 <= channel <= 3:
        raise ValueError("Channel must be an integer between 0 and 3")

    return board.get_pwm_duty(channel + 1)
