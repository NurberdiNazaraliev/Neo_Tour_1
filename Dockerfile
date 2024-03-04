# Use the official Python image from the Docker Hub
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the Docker container
WORKDIR /code

# Install the dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the project files to the working directory in the Docker container
COPY . .
