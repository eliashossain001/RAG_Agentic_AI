import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from modules.modality_encoder import encode_mri_image, encode_text_file
from modules.pdf_parser import extract_text_from_pdf
from db.save_results import save_patient_report

st.set_page_config(page_title="Clinical Dashboard", page_icon="🧠", layout="centered")

st.title("🧠 RAG Agentic AI - Clinical Dashboard")
st.markdown("Upload MRI image, medical history, and doctor-patient conversation to generate a diagnostic report.")

# 1. Upload MRI Image
st.subheader("1. Upload fMRI / MRI Scan Image")
image_file = st.file_uploader("Upload .png or .jpg image", type=["png", "jpg", "jpeg"])
image_summary = encode_mri_image(image_file) if image_file else ""

# 2. Upload Medical History (.txt)
st.subheader("2. Upload Medical History (.txt)")
history_file = st.file_uploader("Upload medical_history_001.txt", type=["txt"])
medical_history_text = encode_text_file(history_file) if history_file else ""

# 3. Upload Doctor-Patient Dialog (.txt)
st.subheader("3. Upload Doctor-Patient Dialog (.txt)")
dialog_file = st.file_uploader("Upload dialog_001.txt", type=["txt"])
dialog_text = encode_text_file(dialog_file) if dialog_file else ""

# 4. Upload Optional PDF Report
st.subheader("4. Upload Additional Doctor Notes or Lab Reports (PDF)")
pdf_file = st.file_uploader("Upload doctor's note or lab report (.pdf)", type=["pdf"])
pdf_summary = extract_text_from_pdf(pdf_file) if pdf_file else "No PDF uploaded."

# Input patient ID
st.subheader("5. Enter Patient ID")
patient_id = st.text_input("Enter unique patient ID")

# Submit button
if st.button("🩺 Run Diagnosis & Generate Report"):
    if not all([patient_id, medical_history_text, dialog_text, image_summary]):
        st.error("Please upload all required files and provide Patient ID.")
    else:
        with st.spinner("Generating diagnosis and recommendations..."):
            # Send request to FastAPI backend
            response = requests.post("http://127.0.0.1:8000/analyze/", json={
                "patient_id": patient_id,
                "medical_history": medical_history_text,
                "dialog": dialog_text,
                "modality_data": image_summary,
                "pdf_summary": pdf_summary
            })

            if response.status_code == 200:
                result = response.json()
                st.success("✅ Report Generated Successfully")
                st.subheader("🩻 Diagnosis")
                st.write(result["diagnosis"])
                st.subheader("⚠️ Risk Prediction")
                st.write(result["risk_prediction"])
                st.subheader("📝 Recommendations")
                st.write(result["recommendations"])
            else:
                st.error(f"API Error: {response.text}")
