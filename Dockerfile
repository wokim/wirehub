# Use an official Python runtime as a parent image
FROM python:3.11.2-slim

# Install required dependencies for smbus
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        python3-dev \
        python3-smbus \
        i2c-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
# ENV NAME World

# Run Gunicorn to start the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
