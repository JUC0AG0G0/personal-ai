from fastapi import FastAPI
from pydantic import BaseModel
from .agent import Agent
import requests
import psutil
import os

app = FastAPI()
agent = Agent()

class PromptRequest(BaseModel):
    prompt: str

class DocsRequest(BaseModel):
    docs: list[str]

@app.get("/")
def root():
    return {"message": "Personal AI Backend Running"}

@app.post("/ask")
def ask_llm(request: PromptRequest):
    response = agent.ask(request.prompt)
    return {"response": response}

@app.post("/add_docs")
def add_docs(request: DocsRequest):
    agent.add_docs(request.docs)
    return {"message": f"{len(request.docs)} documents ajoutés"}

@app.get("/status")
def status():
    host = os.getenv("OLLAMA_HOST")
    models = []
    ollama_reachable = False

    if host:
        try:
            response = requests.get(f"{host}/api/tags", timeout=3)
            if response.status_code == 200:
                models = response.json().get("models", [])
                ollama_reachable = True
        except Exception:
            pass

    return {
        "backend": "running",
        "ollama_reachable": ollama_reachable,
        "models_installed": [m["name"] for m in models],
        "active_model": agent.llm.model_name,
        "active_chats": agent.active_sessions_count()
            if hasattr(agent, "active_sessions_count") else 0,
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
    }

@app.get("/ollama/info")
def ollama_info():
    host = os.getenv("OLLAMA_HOST")
    
    tags = requests.get(f"{host}/api/tags").json()
    ps = requests.get(f"{host}/api/ps").json()

    return {
        "installed_models": tags.get("models", []),
        "running_models": ps.get("models", [])
    }