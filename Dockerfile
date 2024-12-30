# Use official Python runtime as base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install Flask==2.2.3 Flask-MySQLdb==1.0.1 Flask-Mail==0.9.1 mysqlclient==2.2.6

# Expose the default Flask port
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
