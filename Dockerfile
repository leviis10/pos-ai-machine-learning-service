# Use an official Python runtime as a parent image
FROM python:3.12.7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV PYTHONPATH=/app

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]