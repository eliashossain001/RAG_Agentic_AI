import faiss
import pickle
from models.text_embedding import get_embedding

INDEX_PATH = "vector_db/faiss_index.bin"
DOCS_PATH = "vector_db/docs.pkl"

def retrieve_top_k(query, k=3):
    # Load FAISS index and documents
    index = faiss.read_index(INDEX_PATH)
    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)

    query_vector = get_embedding(query).numpy().reshape(1, -1)
    distances, indices = index.search(query_vector, k)

    top_docs = [documents[i] for i in indices[0]]
    return top_docs
