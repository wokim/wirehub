from .DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
import RPi.GPIO as GPIO
import spidev

board = None
spi = None

def init_board():
  global board, spi
  board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
  spi = spidev.SpiDev()

  board.set_adc_enable()
  board.set_pwm_enable()
  board.set_pwm_frequency(1000)

  spi.open(0, 0)  # (bus, device)
  spi.max_speed_hz = 1000000  # SPI Speed: 1MHz

  # Set GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)

  # Set the specified pin as an OUTPUT
  GPIO.setup([i for i in range(22, 28)], GPIO.OUT, initial=GPIO.LOW)
  print(f"GPIO setup complete!")

def cleanup_board():
  GPIO.cleanup()
  spi.close()

def detect_board():
  l = board.detecte()
  print(f"Board list: {l}")

def print_board_status():
  if board.last_operate_status == board.STA_OK:
    print("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    print("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    print("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    print("board status: parameter error")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    print("board status: unsupport board framware version")
