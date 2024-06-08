# Use an official Python runtime as a parent image, based on Alpine
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE $PORT

# Define environment variable for Gunicorn to listen on a specific port
ENV PORT=8000

# Run gunicorn with one worker on the specified port
CMD ["gunicorn", "--workers=1", "--bind", "0.0.0.0:$PORT", "your_application:app"]
