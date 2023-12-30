<!-- # WireHub

## for the Developers
```sh
pip install -r requirements.txt
pip install RPi.GPIO spidev smbus Flask

docker build -t superb .
docker run --device /dev/i2c-1 --privileged -d -p 5000:5000 superb
``` -->
# WireHub

WireHub is a service that provides RESTful APIs for controlling analog input/output, digital input/output, MCP3008 input/output, and PWM on a Raspberry Pi.

## Features
- Control analog input/output.
- Control digital input/output.
- Interface with MCP3008 for analog signal readings.
- Manage PWM (Pulse Width Modulation) for precise control.

## API Documentation
API specifications can be found using Swagger at [http://localhost:5000/apidocs](http://localhost:5000/apidocs).

## Getting Started

### Using Docker
Build the Docker image:
```bash
docker build -t wirehub .
```

Run the Docker container:
```bash
docker run --device /dev/i2c-1 --device /dev/gpiomem --device /dev/spidev0.0 --privileged -d -p 5000:5000 wirehub
```

### For Developers
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python run.py
```

## Contributors

Feel free to contribute by submitting issues or pull requests!
