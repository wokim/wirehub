from flask import Flask
from .api import api_bp
from app.gpio import detect_board, print_board_status, board, init_board, cleanup_board
import time
import atexit

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix='/api')

    atexit.register(cleanup_board)

    return app

def initialize_board():
    detect_board()
    while board.begin() != board.STA_OK:  # Board begin and check board status
        print_board_status()
        logger.error("Board begin failed")
        time.sleep(2)
    print_board_status()
    init_board()
    logger.info("Board begin success")
