# Use an official Python runtime as a parent image
FROM python:3.11.2-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11.2-slim

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    python3-smbus \
    i2c-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Set the working directory and copy application files
WORKDIR /app
COPY . .

# Expose port 5000 for the application
EXPOSE 5000

# Command to run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "--log-level", "info", "run:app"]
