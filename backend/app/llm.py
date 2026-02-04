import subprocess

def ask_ollama(prompt: str) -> str:
    """Envoie un prompt à Ollama et retourne la réponse"""
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Erreur Ollama: {e}"

