import os
from vector_db.init_db import initialize_vector_db

KB_DIR = "data/knowledge_base"
documents = []

for filename in os.listdir(KB_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(KB_DIR, filename), "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                documents.append(content)

if documents:
    initialize_vector_db(documents)
else:
    print("[WARN] No documents found in knowledge_base to index.")
