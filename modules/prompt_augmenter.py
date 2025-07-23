# from modules.modality_encoder import build_context
# from modules.pdf_parser import extract_text_from_pdf
# from retriever.retriever import retrieve_top_k

# def augment_prompt(payload):
#     """
#     Accepts FastAPI payload and returns final prompt and context string.
#     Performs:
#     - Modality encoding
#     - PDF parsing (optional)
#     - Retrieval-Augmented Context (Top-K)
#     """
#     medical_history = payload.medical_history
#     dialog = payload.dialog
#     image_summary = payload.modality_data
#     patient_id = payload.patient_id
#     pdf_summary = payload.pdf_summary

#     # Optional: Try parsing full PDF if pdf_path is provided
#     full_pdf_data = ""
#     if payload.pdf_path:
#         try:
#             full_pdf_data = extract_text_from_pdf(payload.pdf_path)
#         except Exception as e:
#             print(f"[WARN] PDF extraction failed: {e}")

#     # 🔍 Retrieve top-K similar docs using history + dialog as query
#     rag_query = f"{medical_history} {dialog}"
#     retrieved_docs = retrieve_top_k(rag_query)

#     retrieved_section = "\n\n".join([
#         f"[Retrieved Document {i+1}]\n{doc}" for i, doc in enumerate(retrieved_docs)
#     ])

#     # 📄 Build structured context (includes modalities + retrieval + optional PDF)
#     context = (
#         f"{retrieved_section}\n\n"
#         f"[Patient ID] {patient_id}\n"
#         f"[Medical History]\n{medical_history}\n\n"
#         f"[Doctor-Patient Dialog]\n{dialog}\n\n"
#         f"[Image Analysis Summary]\n{image_summary}\n\n"
#         f"[PDF Summary (EHR/Lab)]\n{pdf_summary}\n\n"
#     )

#     if full_pdf_data:
#         context += f"[Full PDF Content Extracted]\n{full_pdf_data[:1000]}..."

#     # 🧠 Instruction prompt for the multi-agent system
#     prompt = (
#         "You are a clinical AI assistant. Based on the retrieved evidence, image analysis, and patient conversation, "
#         "provide a diagnosis, assess risk, and offer recommendations tailored to this patient."
#     )

#     return prompt, context

from modules.modality_encoder import build_context
from retriever.retriever import retrieve_top_k

def augment_prompt(payload):
    """
    Accepts FastAPI payload and returns final prompt and context string.
    Performs:
    - Modality encoding
    - Retrieval-Augmented Context (Top-K)
    - Includes optional PDF summary (already provided in payload)
    """
    medical_history = payload.medical_history
    dialog = payload.dialog
    image_summary = payload.modality_data
    patient_id = payload.patient_id
    pdf_summary = payload.pdf_summary  # ✅ already parsed, no need for path

    # 🔍 Retrieve top-K similar docs using history + dialog as query
    rag_query = f"{medical_history} {dialog}"
    retrieved_docs = retrieve_top_k(rag_query)

    retrieved_section = "\n\n".join([
        f"[Retrieved Document {i+1}]\n{doc}" for i, doc in enumerate(retrieved_docs)
    ])

    # 📄 Build structured context (includes modalities + retrieval + optional PDF)
    context = (
        f"{retrieved_section}\n\n"
        f"[Patient ID] {patient_id}\n"
        f"[Medical History]\n{medical_history}\n\n"
        f"[Doctor-Patient Dialog]\n{dialog}\n\n"
        f"[Image Analysis Summary]\n{image_summary}\n\n"
        f"[PDF Summary (EHR/Lab)]\n{pdf_summary}\n\n"
    )

    # 🧠 Instruction prompt for the multi-agent system
    prompt = (
        "You are a clinical AI assistant. Based on the retrieved evidence, image analysis, and patient conversation, "
        "provide a diagnosis, assess risk, and offer recommendations tailored to this patient."
    )

    return prompt, context
