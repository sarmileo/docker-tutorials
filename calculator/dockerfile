# Use Python as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY calculator.py /app/

# Install any dependencies (if needed)
# Using RUN to demonstrate execution at build time
RUN echo "Building the Docker image and setting up the environment..."

# Use ENTRYPOINT to ensure the script is always run with Python
ENTRYPOINT ["python", "calculator.py"]

# Set a default CMD for the container
CMD ["add", "10", "20"]