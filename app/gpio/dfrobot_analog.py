from . import board

def read_analog_from_dfrobot(channel):
    """
    Read the analog value from a specified channel of the DFRobot Expansion Board.

    The DFRobot Expansion Board features an on-board MCU (STM32) and a 12-bit ADC.
    It allows reading from four groups of analog ports (A0-A3). The input voltage
    received from the analog sensor is converted to a 12-bit digital value by the ADC.
    This digital data is then sent to the Raspberry Pi via I2C communication.

    Args:
        channel (int): The channel number (0-3) to read from.

    Returns:
        int: The 12-bit digital value (0-4095) representing the analog input voltage.

    Raises:
        ValueError: If the specified channel is out of the acceptable range.
    """
    if not 0 <= channel <= 3:
        raise ValueError("Channel must be an integer between 0 and 3")

    try:
        # Reading analog value from the specified channel
        analog_value = board.get_adc_value(channel + 1)  # Adding 1 because DFRobot channels start from 1
        return analog_value
    except Exception as e:
        raise Exception(f"Failed to read from DFRobot analog channel {channel}: {e}")
