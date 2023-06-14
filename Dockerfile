FROM python:3.9

WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script files
COPY promnist.py /
COPY testcode.py /

# Copy the rest of your project files
COPY . .

# Set the command to run your Python program
CMD ["python", "testcode.py"]

