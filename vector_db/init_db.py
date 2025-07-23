import faiss
import numpy as np
import os
from models.text_embedding import get_embedding

# Define the path to save the FAISS index
INDEX_DIR = os.path.dirname(__file__)
INDEX_PATH = os.path.join(INDEX_DIR, "knowledge_base.index")

def initialize_vector_db(documents):
    print("[INFO] Initializing FAISS vector DB with embeddings...")

    try:
        # Get embeddings for all documents
        vectors = [get_embedding(doc).cpu().numpy() for doc in documents]

        # Create FAISS index
        dim = vectors[0].shape[0]
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(vectors))  # ✅ Correct method

        # Ensure the directory exists
        os.makedirs(INDEX_DIR, exist_ok=True)

        # Save the index
        faiss.write_index(index, INDEX_PATH)
        print(f"[SUCCESS] FAISS index built and saved to: {INDEX_PATH}")

    except Exception as e:
        print(f"[ERROR] Failed to initialize vector DB: {e}")
