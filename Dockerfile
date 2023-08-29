# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY ./app /app

# Update system packages and install build tools
RUN apt-get update && apt-get install -y \
	build-essential \
	cmake \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install the required packages from requirements.txt
RUN pip install agent-dingo "typer[all]"

# Run the application
CMD ["python", "cli.py", "hello", "Docker"]