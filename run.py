import logging
from app import create_app
from app.gpio import detect_board, print_board_status, board, init_board, cleanup_board
import atexit
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

def initialize_board():
    detect_board()
    while board.begin() != board.STA_OK:  # Board begin and check board status
        print_board_status()
        logger.error("Board begin failed")
        time.sleep(2)
    print_board_status()
    init_board()
    logger.info("Board begin success")

atexit.register(cleanup_board)

if __name__ == '__main__':
    try:
        initialize_board()
        app.run(debug=True, port=5000, host='0.0.0.0')
    finally:
        # Cleanup GPIO to release resources
        cleanup_board()
