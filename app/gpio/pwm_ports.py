from . import board

def set_pwm_duty(pin, value):
    '''
      @brief    Get selected channel duty
      @param pin:int One channel to set, items in range 1 to 4
      @param duty: float    Duty to set, in range 0.0 to 100.0
    '''
    board.set_pwm_duty(pin, value)

def get_pwm_duty(pin):
    '''
      @brief    Get selected channel duty
      @param pin:int One channel to get, items in range 1 to 4
    '''
    return board.get_pwm_duty(pin)
