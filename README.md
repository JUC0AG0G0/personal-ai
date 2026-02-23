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


## Roadmap

TODO: Ajout un controller permettant de voir l'etat du llm

    - Model dispo
    - Model up
    - Parametres
    - Infos en tout genre

TODO: Ajout Swagger

TODO: Rag

TODO: Interface web basique

    - chat
    - page status
    - Page de configuration du model

TODO: Enregistrememnt du contexte pour que tout les environement utilise les meme parametres.

TODO: CORS

TODO: Systeme d'utilisateur avec authentification (jwt)

    - Système d'auth front
    - Sécurisation de l'api

TODO: Gestion des users

    - Possibilité de créé des users
    - Possibilité de faire une demande d'acces.
    - Gérer les demande d'acces.
    - Envoie de mails avec identifiants
    - Réninitalisation de mot de passe

TODO: Sécurité

    - Rate limit
    - Sécurisation des routes (role et connecté)

TODO: Pipeline

### V1

TODO: Opti

TODO: Améliorer le front

TODO: Gestionnaire de charge