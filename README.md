# Personal AI Assistant

Projet d'IA personnelle locale avec :

- LLM local via Ollama
- Backend FastAPI
- RAG avec base vectorielle
- Interface Web React / Next.js
- Dockerisation complète
- Déploiement VPS

## Architecture

backend → API + agent IA  
frontend → interface utilisateur  
infra → docker + nginx + config serveur  


Exemple requette :
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"prompt": "Dis-moi bonjour comme un pirate."}'
