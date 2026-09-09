FROM python:3.11-slim
WORKDIR /app
COPY src/ ./src/
COPY requirements.txt ./
ENV PYTHONPATH=/app/src
RUN apt-get update && apt-get install -y procps
RUN pip install --no-cache-dir -r requirements.txt