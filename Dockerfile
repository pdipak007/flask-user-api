# Use a small Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your current project folder to container
COPY . /app

# Install Flask from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 so we can access the app
EXPOSE 5000

# Run the app when the container starts
CMD ["python", "app.py"]
