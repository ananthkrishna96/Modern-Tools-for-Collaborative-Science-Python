FROM python:3.9

# Install required dependencies
RUN pip install numpy matplotlib scipy

# Copy your code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Define the entry point command
CMD ["python", "promnist.py"]

