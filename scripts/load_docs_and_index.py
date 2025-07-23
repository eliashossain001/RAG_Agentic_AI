import os
import sys
from tqdm import tqdm  # ✅ Added tqdm import

# Append root project path to sys.path for module resolution
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

from vector_db.init_db import initialize_vector_db

# Path to the knowledge base directory
knowledge_base_dir = os.path.join(ROOT_DIR, 'data', 'knowledge_base')

# Collect all .txt documents with tqdm progress bar
docs = []
txt_files = [f for f in os.listdir(knowledge_base_dir) if f.endswith('.txt')]
for filename in tqdm(txt_files, desc="Loading knowledge base files"):
    file_path = os.path.join(knowledge_base_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()
        if text:
            docs.append(text)

# Check if documents are found
if not docs:
    print("[WARNING] No .txt documents found in knowledge_base directory.")
else:
    print(f"[INFO] Loaded {len(docs)} documents from knowledge base.")
    initialize_vector_db(docs)
    print("[SUCCESS] Vector DB initialized.")
