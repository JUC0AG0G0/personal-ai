import requests
import json

class LLMManager:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.api_url = "http://personal_ai_ollama:11434/api/generate"

    def generate(self, prompt: str) -> str:
        payload = {"model": self.model_name, "prompt": prompt}
        try:
            resp = requests.post(self.api_url, json=payload, stream=True)
            resp.raise_for_status()
            text = ""
            for line in resp.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        text += data.get("response", "")
                    except json.JSONDecodeError:
                        pass
            return text.strip()
        except Exception as e:
            return f"Erreur Ollama API: {e}"
