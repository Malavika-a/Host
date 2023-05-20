# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose the port on which the Django development server will run (default: 8000)
EXPOSE 8000

# Define the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Copy the project code into the container
COPY . .

ENV PYTHONPATH=/

# Define the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]