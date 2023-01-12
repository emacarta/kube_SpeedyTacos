# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required packages
RUN pip install pandas psycopg2 lxml

# Copy the rest of the application code into the container
COPY . .

# Run the main script
CMD ["python", "main.py"]