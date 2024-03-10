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

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Specify the command to run on container start
# Here, gunicorn is used as the WSGI server to serve the Flask app.
# The app is served on 0.0.0.0:5000, and `run:app` points to the Flask app instance in the run.py file.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "--log-level", "info", "run:app"]
