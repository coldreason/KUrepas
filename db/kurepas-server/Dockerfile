# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV MYSQL_DATABASE=kurepas
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Password12!
ENV MYSQL_HOST=db

# Expose the default Flask port
EXPOSE 5000

# Run the command to start the Flask application
CMD ["flask", "run"]