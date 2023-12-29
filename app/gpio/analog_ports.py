from . import board

def read_analog(pin):
    '''
      @brief    Get adc value
      @param pin: int    Channel to get, in range 1 to 4
    '''
    val = board.get_adc_value(pin)
    return val
