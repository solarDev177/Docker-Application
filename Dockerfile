FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy all the files from your project to the container
COPY . /app

# Install Python dependencies
RUN pip install colorama

# Expose the terminal port (optional)
EXPOSE 8000

# Prevent the console recursion by not running the new console instance
CMD ["python", "unit_converter.py"]
