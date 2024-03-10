from app import create_app
from app.gpio import detect_board, print_board_status, board, init_board, cleanup_board
import atexit
import time

app = create_app()

def initialize_board():
    detect_board()
    while board.begin() != board.STA_OK:  # Board begin and check board status
        print_board_status()
        print("Board begin failed")
        time.sleep(2)
    print_board_status()
    init_board()
    print("Board begin success")

atexit.register(cleanup_board)

if __name__ == '__main__':
    try:
        initialize_board()
        app.run(debug=True, port=5000, host='0.0.0.0')
    finally:
        # Cleanup GPIO to release resources
        cleanup_board()
