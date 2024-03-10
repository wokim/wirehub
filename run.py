import logging
from app import create_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
