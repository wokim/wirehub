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
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Start the Flask app
CMD ["python", "run.py"]
