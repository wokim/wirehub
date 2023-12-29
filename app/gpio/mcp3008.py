from . import spi

def read_adc(pin):
    adc = spi.xfer2([1, (8 + pin) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data
