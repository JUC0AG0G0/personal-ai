from .llm_manager import LLMManager

class Agent:
    def __init__(self):
        self.llm = LLMManager()

    def ask(self, prompt: str) -> str:
        """
        Ici on pourrait ajouter :
        - pré-traitement du prompt
        - ajout de contexte/mémoire
        - gestion RAG
        """
        response = self.llm.generate(prompt)
        # Exemple post-traitement simple
        return response
