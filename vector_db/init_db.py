import os
import faiss
import pickle
from models.text_embedding import get_embedding

INDEX_PATH = "vector_db/faiss_index.bin"
DOCS_PATH = "vector_db/docs.pkl"

def initialize_vector_db(documents):
    # Create FAISS index
    dimension = 384  # for MiniLM-L6-v2
    index = faiss.IndexFlatL2(dimension)
    vectors = []
    
    for doc in documents:
        embedding = get_embedding(doc)
        vectors.append(embedding)

    index.add_batch([v.numpy() for v in vectors])

    # Save index and docs
    faiss.write_index(index, INDEX_PATH)
    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)

    print(f"[VectorDB] Index initialized with {len(documents)} documents")
