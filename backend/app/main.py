from fastapi import FastAPI
from pydantic import BaseModel
from .agent import Agent

app = FastAPI()
agent = Agent()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Personal AI Backend Running"}

@app.post("/ask")
def ask_llm(request: PromptRequest):
    response = agent.ask(request.prompt)
    return {"response": response}
