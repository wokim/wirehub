# WireHub

WireHub is a service that provides RESTful APIs for controlling analog input/output, digital input/output, PWM, and reading analog inputs through MCP3008 on a Raspberry Pi using the DFRobot Expansion HAT. This HAT extends the capabilities of the Raspberry Pi, enabling precise control and interfacing with various electronic components.

For more information about the DFRobot Expansion HAT, visit [DFRobot Expansion HAT for Raspberry Pi](https://wiki.dfrobot.com/IO%20Expansion%20HAT%20for%20Raspberry%20Pi%20%20SKU%3A%20%20DFR0566).

## Features

- Control digital input/output using DFRobot Expansion HAT.
- Read analog inputs directly through DFRobot Expansion HAT.
- Manage PWM (Pulse Width Modulation) for precise control using DFRobot Expansion HAT.
- Interface with MCP3008 for additional analog signal readings using the SPI interface on the DFRobot Expansion HAT.

## Quick Start

To quickly start using the WireHub project, you can pull the Docker image from Docker Hub and run it with the following command:

```bash
# Enable I2C and SPI on your Raspberry Pi
$ sudo raspi-config

# Pull the latest WireHub Docker image from Docker Hub and run it using the following command:
$ docker run --device /dev/i2c-1 --device /dev/gpiomem --device /dev/spidev0.0 --privileged -d -p 5000:5000 wokim/wirehub:latest
```

## API Documentation

Below is the documentation for the available API endpoints, including their paths, methods, descriptions, and example request bodies for PUT methods.

| Path                          | Method | Description                                                         | Request Parameters                         | Example Request Body for PUT                  | Example Response Body                   |
| ----------------------------- | ------ | ------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------- | --------------------------------------- |
| `/api/gpio/digital/<int:pin>` | GET    | Read the digital input value from a specified GPIO pin.             | `pin`: A GPIO pin number for digital I/O   | N/A                                           | `{"pin": 5, "value": 1}`                |
| `/api/gpio/digital/<int:pin>` | PUT    | Write a digital output value to a specified GPIO pin.               | `pin`: A GPIO pin number for digital I/O   | `{"value": true}` or `{"value": false}`       | `{"pin": 5, "value": 1}`                |
| `/api/gpio/pwm/<int:pin>`     | GET    | Read the PWM duty cycle value from a specified pin.                 | `pin`: A GPIO pin number for PWM output    | N/A                                           | `{"pin": 1, "value": 50.5}`             |
| `/api/gpio/pwm/<int:pin>`     | PUT    | Write a PWM duty cycle value to a specified pin.                    | `pin`: A GPIO pin number for PWM output    | `{"value": 50.0}` (value range: 0.0 to 100.0) | `{"pin": 1, "value": 50.5}`             |
| `/api/gpio/analog/<int:pin>`  | GET    | Read the analog value from a specified DFRobot Expansion Board pin. | `pin`: A GPIO pin number for analog input  | N/A                                           | `{"pin": 2, "value": 1023, "bits": 12}` |
| `/api/gpio/mcp3008/<int:pin>` | GET    | Read the analog value from a specified MCP3008 channel.             | `pin`: A channel number on the MCP3008 ADC | N/A                                           | `{"pin": 3, "value": 512, "bits": 12}`  |
| `/api/gpio/status`            | GET    | Get the status of all GPIO pins.                                    | None                                       | N/A                                           | N/A                                     |

Please replace `<int:pin>` with the actual pin number when making requests.

## Getting Started

### Prerequisites

Before running the WireHub service, ensure that the `I2C` and `SPI` interfaces are enabled on your Raspberry Pi as they are essential for communication with the DFRobot Expansion HAT and MCP3008.

#### Enabling I2C and SPI

1. Open the Raspberry Pi configuration tool in the terminal:

   ```sh
   sudo raspi-config
   ```

2. Navigate to `Interfacing Options` > `I2C` and select `<Yes>` to enable the I2C interface.
3. For SPI, navigate to `Interfacing Options` > `SPI` and select `<Yes>` to enable the SPI interface.
4. Finish and reboot your Raspberry Pi for the changes to take effect.

### Using Docker

Build the Docker image:

```bash
docker build -t wirehub .
```

Run the Docker container:

```bash
docker run --device /dev/i2c-1 --device /dev/gpiomem --device /dev/spidev0.0 --privileged -d -p 5000:5000 --log-opt max-size=10m --log-opt max-file=3 wirehub
```

### For Developers

#### Setting up a virtual environment

It's recommended to create a virtual environment for the project dependencies. You can do this by running:

```bash
# Create a virtual environment named '.venv'
python3 -m venv .venv

# Activate the virtual environment:
source .venv/bin/activate
```

#### Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### Run the application:

```bash
python run.py
```

## Contributors

Feel free to contribute by submitting issues or pull requests!
