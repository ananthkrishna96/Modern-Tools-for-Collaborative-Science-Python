FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY promnist.py /
COPY testcode.py /
COPY . .

CMD ["python", "promnist.py"]

