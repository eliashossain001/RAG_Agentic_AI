# from fastapi import FastAPI
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import os

# from modules.prompt_augmenter import augment_prompt
# from agents.diagnosis_agent import DiagnosisAgent
# from agents.risk_prediction_agent import RiskPredictionAgent
# from agents.recommendation_agent import RecommendationAgent
# from db.save_results import save_patient_report

# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")
# if not API_KEY:
#     raise RuntimeError("GOOGLE_API_KEY not found in .env")

# app = FastAPI()

# class InputPayload(BaseModel):
#     patient_id: str
#     medical_history: str
#     dialog: str
#     modality_data: str  # MRI or scan summary
#     pdf_path: str = None  # Optional PDF file path
#     pdf_summary: str  # ✅ Required summary from parsed PDF

# @app.post("/analyze/")
# def analyze_patient(payload: InputPayload):
#     prompt, context = augment_prompt(payload)

#     # Run agentic reasoning
#     diagnosis = DiagnosisAgent().run(prompt, context)
#     risk = RiskPredictionAgent().run(prompt, context)
#     recs = RecommendationAgent().run(prompt, context)

#     # ✅ Save to database with PDF summary included
#     save_patient_report(
#         patient_id=payload.patient_id,
#         diagnosis=diagnosis,
#         risk=risk,
#         recommendations=recs,
#         pdf_summary=payload.pdf_summary
#     )

#     return {
#         "diagnosis": diagnosis,
#         "risk_prediction": risk,
#         "recommendations": recs
#     }

# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from modules.prompt_augmenter import augment_prompt
from agents.multi_agent_executor import run_multi_agent_system

app = FastAPI()

class AnalyzePayload(BaseModel):
    patient_id: str
    medical_history: str
    dialog: str
    modality_data: str
    pdf_summary: str = ""

@app.post("/analyze/")
def analyze_patient(payload: AnalyzePayload):
    prompt, context = augment_prompt(payload)

    responses = run_multi_agent_system(
        prompt=prompt,
        context=context,
        patient_id=payload.patient_id,
        image_path=None  # You can pass image path here if available
    )

    return {
        "diagnosis": responses["Diagnosis"],
        "risk_prediction": responses["Risk Prediction"],
        "recommendations": responses["Recommendations"],
        "guidelines": responses["Guidelines Advisor"]
    }
