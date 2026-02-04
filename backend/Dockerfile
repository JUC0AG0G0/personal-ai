FROM python:3.11-slim

WORKDIR /app

# Installer dépendances système
RUN apt-get update && \
    apt-get install -y curl git unzip zstd && \
    rm -rf /var/lib/apt/lists/*

# Installer Ollama
RUN curl -s https://ollama.com/install.sh | bash

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code backend
COPY . .

# Copier script entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]


# Entrypoint pour lancer daemon et uvicorn
ENTRYPOINT ["/app/entrypoint.sh"]
