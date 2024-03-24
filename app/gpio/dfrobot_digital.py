import RPi.GPIO as GPIO

def read_digital_pin(pin):
    """
    Read the digital input value from a specified digital port of the DFRobot Expansion Board.
    
    The DFRobot Expansion Board provides 28 groups (D0-D27) of digital ports, which are
    mapped to the Raspberry Pi GPIO pins GPIO0~GPIO27 (BCM coding scheme).
    
    Args:
        pin (int): The GPIO pin number (BCM coding) to read from, in the range of 0 to 27.
    
    Returns:
        bool: The current digital value of the specified GPIO pin (True for GPIO.HIGH, False for GPIO.LOW).
    
    Raises:
        ValueError: If the specified pin is out of the acceptable range.
    """
    if not 0 <= pin <= 27:
        raise ValueError("Pin number must be in the range 0 to 27")

    try:
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)
    except Exception as e:
        raise Exception(f"Failed to read digital pin {pin}: {e}")

def write_digital_pin(pin, value):
    """
    Write a digital output value to a specified digital port of the DFRobot Expansion Board.
    
    This function allows setting the digital state of one of the 28 digital ports (D0-D27)
    provided by the DFRobot Expansion Board, corresponding to Raspberry Pi GPIO pins GPIO0~GPIO27.
    
    Args:
        pin (int): The GPIO pin number (BCM coding) to write to, in the range of 0 to 27.
        value (bool or int): The digital value to set on the GPIO pin (True, False, 1, or 0).
    
    Raises:
        ValueError: If the specified pin is out of the acceptable range or value is not True, False, 1, or 0.
    """
    if not 0 <= pin <= 27:
        raise ValueError("Pin number must be in the range 0 to 27")

    if value not in [True, False, 1, 0]:
        raise ValueError("Value must be either True, False, 1, or 0")

    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH if value in [True, 1] else GPIO.LOW)
    except Exception as e:
        raise Exception(f"Failed to write digital pin {pin}: {e}")
