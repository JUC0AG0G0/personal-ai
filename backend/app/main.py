from fastapi import FastAPI
from pydantic import BaseModel
from .llm import ask_ollama

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Personal AI Backend Running"}

@app.post("/ask")
def ask_llm(request: PromptRequest):
    response = ask_ollama(request.prompt)
    return {"response": response}