# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && mkdir app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN python script.py -rs

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
