import RPi.GPIO as GPIO

def get_digital_input(pin):
    try:
        # Set GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)

        # Set the specified pin as an INPUT
        GPIO.setup(pin, GPIO.OUT)

        return GPIO.input(pin)

    except Exception as e:
        print(f"Error getting GPIO pin {pin}: {e}")


def set_digital_output(pin, value):
    """
    Set the digital output of the specified GPIO pin.

    Parameters:
    - pin (int): The GPIO pin number.
    - value (bool): True for HIGH (1), False for LOW (0).
    """
    try:
         # Set GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)

        # Set the specified pin as an OUTPUT
        GPIO.setup(pin, GPIO.OUT)

        # Set the digital output value
        GPIO.output(pin, GPIO.HIGH if value else GPIO.LOW)

        print(f"GPIO pin {pin} set to {'HIGH' if value else 'LOW'}")

    except Exception as e:
        print(f"Error setting GPIO pin {pin}: {e}")
