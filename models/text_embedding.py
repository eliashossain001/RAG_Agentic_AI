from sentence_transformers import SentenceTransformer

# Load a compact but effective model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    return embedding_model.encode(text, convert_to_tensor=True)
