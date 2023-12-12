from . import board

def read_analog(port):
    val = board.get_adc_value(port)
    return val