FROM python:3.11.0-bullseye

WORKDIR /app

COPY . .

CMD ["python3", "stream.py"]
