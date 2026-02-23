#!/bin/bash

echo "Backend démarré, connexion à Ollama sur $OLLAMA_HOST"

exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --reload-dir /app