# agents/multi_agent_executor.py

from agents.diagnosis_agent import DiagnosisAgent
from agents.risk_prediction_agent import RiskPredictionAgent
from agents.recommendation_agent import RecommendationAgent
from agents.guidelines_advisor_agent import GuidelinesAdvisorAgent

# Optional: for saving/logging multi-turn agent feedback
from db.save_results import save_patient_report

def run_multi_agent_system(prompt, context, patient_id, pdf_summary="", image_path=None):
    responses = {}

    # Each agent receives a specialized view of the same prompt/context
    responses["Diagnosis"] = DiagnosisAgent().run(
        prompt + "\nFocus on identifying possible mental health conditions.",
        context,
        image_path
    )

    responses["Risk Prediction"] = RiskPredictionAgent().run(
        prompt + "\nAssess any risks or symptoms worsening.",
        context
    )

    responses["Recommendations"] = RecommendationAgent().run(
        prompt + "\nGive actionable next steps or therapy suggestions.",
        context
    )

    responses["Guidelines Advisor"] = GuidelinesAdvisorAgent().run(
        prompt + "\nSummarize relevant treatment guidelines from retrieved documents.",
        context
    )

    # ✅ Log all outputs, including guidelines and optional PDF summary
    save_patient_report(
        patient_id=patient_id,
        diagnosis=responses["Diagnosis"],
        risk=responses["Risk Prediction"],
        recommendations=responses["Recommendations"],
        pdf_summary=pdf_summary,
        guideline_summary=responses["Guidelines Advisor"]
    )

    return responses
