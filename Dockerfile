# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#RUN pip install python-nicknames python-Levenshtein
# Make port 80 available to the world outside this container
EXPOSE 80

# Run name_processor.py when the container launches
CMD ["python", "src/main.py"]
