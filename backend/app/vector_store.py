from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document

class VectorStore:
    def __init__(self, persist_dir="chroma_db"):
        self.persist_dir = persist_dir
        self.db = Chroma(persist_directory=persist_dir, embedding_function=OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://ollama:11434"
)
)

    def add_documents(self, docs: list[Document]):
        """Ajoute des documents à la base vectorielle"""
        self.db.add_documents(docs)

    def query(self, query_text: str, k: int = 3):
        """Récupère les k documents les plus pertinents"""
        return self.db.similarity_search(query_text, k=k)
