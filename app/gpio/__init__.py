import logging
from .DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
import RPi.GPIO as GPIO
import spidev

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
spi = spidev.SpiDev()

def init_board():
  cleanup_board()
  
  board.set_adc_enable()
  board.set_pwm_enable()
  board.set_pwm_frequency(1000)

  spi.open(0, 0)  # (bus, device)
  spi.max_speed_hz = 1000000  # SPI Speed: 1MHz

  # Set GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)

  pins = [20, 21, 22, 23, 24, 25, 26, 27]
  # pins = [0, 1, 2, 3, 4, 5, 6, 7]

  for pin in pins:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)

  # Set the specified pin as an OUTPUT
  logger.info(f"GPIO setup complete!")

def cleanup_board():
  GPIO.cleanup()
  spi.close()

def detect_board():
  l = board.detecte()
  logger.info(f"Board list: {l}")

def print_board_status():
  if board.last_operate_status == board.STA_OK:
    logger.info("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    logger.error("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    logger.error("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    logger.error("board status: parameter error")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    logger.error("board status: unsupport board framware version")
