from . import spi

def read_analog_from_mcp3008(channel):
    """
    Read the analog value from a specified channel of the MCP3008 ADC.

    The MCP3008 is a 10-bit ADC (Analog to Digital Converter). It converts analog inputs 
    to digital values with a resolution of 10 bits (0-1023).

    Args:
        channel (int): The MCP3008 channel (0-7) to read from.

    Returns:
        int: The analog value read from the specified channel (0-1023).

    Raises:
        ValueError: If the specified channel is out of range.
        IOError: If there's a communication error with the MCP3008.
    """
    if not 0 <= channel <= 7:
        raise ValueError("Channel must be an integer between 0 and 7")

    try:
        # Start bit (1), single-ended bit (1), and D2, D1, D0 bits for channel selection
        # in the 24-bit command sent to MCP3008 to read a channel.
        command = [1, (8 + channel) << 4, 0]
        adc_response = spi.xfer2(command)

        # Combine the response (adc_response[1] & 3 << 8) + adc_response[2] to get the 10-bit result.
        adc_value = ((adc_response[1] & 3) << 8) + adc_response[2]
        return adc_value

    except Exception as e:
        raise IOError(f"Failed to read from MCP3008 channel {channel}: {e}")
