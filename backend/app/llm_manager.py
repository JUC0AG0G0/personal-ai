import subprocess

class LLMManager:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        """Appelle Ollama pour générer une réponse"""
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Erreur Ollama: {e}"
