
# RAG_Agentic_AI: Multi-Agent Clinical Reasoning Framework

This project implements a Retrieval-Augmented Generation (RAG) based Multi-Agent Clinical AI System for diagnosis, risk prediction, treatment recommendation, and guideline summarization.

---

## 📁 Project Structure

```
RAG_Agentic_AI/
│
├── agents/                  # LLM-based agents (diagnosis, risk, recommendations, guidelines)
├── app/                     # FastAPI backend
├── data/                    # Contains user uploads and knowledge_base
│   └── knowledge_base/      # .txt files for retrieval
├── db/                      # patient_reports.db saved here
├── models/                  # Embedding model
├── modules/                 # Modality encoding, PDF parsing
├── retriever/               # FAISS-based retriever
├── scripts/                 # Synthetic data generator, loader, utils
├── streamlit_app/           # Frontend Streamlit UI
├── utils/                   # Misc helper utilities
├── vector_db/               # Vector DB init + store
├── .env                     # Environment vars (e.g. OpenAI/Gemini keys)
├── requirements.txt         # Install dependencies
└── README.md                # This file
```

---

## Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/RAG_Agentic_AI.git
cd RAG_Agentic_AI
```

### 2. Create Virtual Environment

```bash
python -m venv eliasenv
source eliasenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Initialization

### Step 1: Populate `knowledge_base`

Place `.txt` files (e.g., clinical notes, guidelines, summaries) into:
```
data/knowledge_base/
```

Example:
```
- anxiety_overview.txt
- brain_mri_notes.txt
- treatment_guidelines.txt
```

### Step 2: Initialize Vector DB

```bash
python scripts/load_docs_and_index.py
```

This builds your FAISS vector database using `sentence-transformers`.

---

## Run the Backend

```bash
uvicorn app.main:app --reload
```

Backend available at: `http://127.0.0.1:8000`

---

## 🌐 Run the Streamlit Frontend

```bash
streamlit run streamlit_app/interface.py
```

Streamlit will open a web browser for file upload and chatbot interaction.

---

## 🤖 Multi-Agent System

Agents included:
- `DiagnosisAgent` – generates condition hypotheses.
- `RiskPredictionAgent` – assesses worsening symptoms or risks.
- `RecommendationAgent` – gives therapy and action suggestions.
- `GuidelinesAdvisorAgent` – summarizes clinical best practices.

Each agent receives the same `prompt` + `context` and returns a unique output.

---

## 📂 Logging Reports

All multi-agent responses are saved in a SQLite DB:

```
patient_reports.db
```

Fields:
- patient_id
- diagnosis
- risk_prediction
- recommendations
- pdf_summary
- guidelines_summary ✅ (automatically logged now)

---

## 🧪 Generating Synthetic Data (Optional)

To generate 10,000 synthetic files for testing:

```bash
python scripts/generate_synthetic_kb.py --num_samples 10000
```

This creates diverse `.txt` files under:
```
data/knowledge_base/
```

Then re-run:
```bash
python scripts/load_docs_and_index.py
```

---

## 📥 Upload Format

Via Streamlit, upload:
- 🧾 Medical History (`.txt`)
- 🗣️ Doctor-Patient Dialog (`.txt`)
- 🖼️ Image summary (optional)
- 📄 EHR PDF or Summary (optional)

All inputs are used to create a RAG-enhanced prompt.

---

## 🔒 Environment Setup

Create a `.env` file with:

```
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

---

## 📈 Future Plans

- Add multimodal vision model support
- Include LLaMA/Gemma via Hugging Face
- Export reports to PDF
- Enable memory + multi-turn patient threads

---

## 👨‍💼 Author

**Elias Hossain**  
_Machine Learning Researcher | PhD Student | AI x Reasoning Enthusiast_

[![GitHub](https://img.shields.io/badge/GitHub-EliasHossain001-blue?logo=github)](https://github.com/EliasHossain001)

---

## 📝 License

MIT License — Free to use, distribute, and modify.

