from .llm_manager import LLMManager
from .vector_store import VectorStore
from langchain_core.documents import Document

class Agent:
    def __init__(self):
        self.llm = LLMManager()
        self.vstore = VectorStore()

    def add_docs(self, docs: list[str]):
        doc_objects = [Document(page_content=d) for d in docs]
        self.vstore.add_documents(doc_objects)

    def ask(self, prompt: str) -> str:
        docs = self.vstore.query(prompt)
        context = "\n".join([d.page_content for d in docs])
        
        augmented_prompt = (
            f"Utilise les informations suivantes pour répondre à la question.\n"
            f"Réponds dans la même langue que la question.\n\n"
            f"Contexte :\n{context}\n\n"
            f"Question : {prompt}"
        )
        
        response = self.llm.generate(augmented_prompt)
        return response

