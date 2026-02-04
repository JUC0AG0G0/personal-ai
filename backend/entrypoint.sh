#!/bin/bash

# Lancer Ollama server en arrière-plan
ollama serve &

# Attendre que le serveur démarre
sleep 5

# Vérifier si le modèle Mistral est présent
if ! ollama list | grep -q llama3; then
    echo "Téléchargement du modèle Llama3..."
    ollama pull llama3
fi

# Lancer Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
