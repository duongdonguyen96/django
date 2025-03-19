# Use the official Python image from the Docker Hub, version 3.11
FROM python:3.11

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire source code into the container
COPY . .

# Expose port 8000 for the Django application
EXPOSE 8000

# Command to run the Gunicorn server when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]