FROM ollama/ollama:latest

# Installer curl (si besoin)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Pull des modèles au build (optionnel, ou tu peux les pull au runtime)
RUN ollama pull llama3:8b
RUN ollama pull nomic-embed-text

CMD ["serve"]