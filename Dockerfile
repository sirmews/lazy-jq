# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

# Install the required packages from requirements.txt
RUN pip install langchain openai python-dotenv "typer[all]"

ENTRYPOINT ["python", "cli.py"]