FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl git unzip zstd && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV OLLAMA_HOST=http://personal_ai_ollama:11434

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]