# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
libgl1-mesa-glx \
libglib2.0-0 \
python3-tk \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& mkdir ai

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /ai

# Copy the current directory contents into the container at /usr/src/app
COPY . /ai

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8888

# Run detect_and_track.py with the specified source when the container launches
CMD ["python", "detect_and_track.py", "--loop", "static/json/example_loop.json", "--source", "static/video/test1.MP4", "--filename", "123"]
