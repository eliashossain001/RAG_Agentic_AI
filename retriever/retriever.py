import faiss
import os
from models.text_embedding import get_embedding

# Correct path to saved FAISS index
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../vector_db/knowledge_base.index")

def retrieve_top_k(query, k=3):
    # Load index
    index = faiss.read_index(INDEX_PATH)

    # Get embedding of the query
    query_vector = get_embedding(query).cpu().numpy().reshape(1, -1)

    # Search FAISS index
    distances, indices = index.search(query_vector, k)

    # Return dummy results (you can later map `indices` to actual docs)
    return [f"Retrieved doc #{i} (distance: {dist:.2f})" for i, dist in zip(indices[0], distances[0])]
