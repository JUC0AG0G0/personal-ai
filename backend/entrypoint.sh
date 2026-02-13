#!/bin/bash

echo "Backend démarré, connexion à Ollama sur $OLLAMA_HOST"

# Lancer Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
