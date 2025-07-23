# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("models/gemini-2.0-flash")

# class RiskPredictionAgent:
#     def run(self, prompt: str, context: str) -> str:
#         full_prompt = (
#             "You are a clinical risk evaluator. Based on the patient's data, assess their likelihood of relapse or symptom worsening.\n\n"
#             f"Context:\n{context}\n\n"
#             f"Prompt:\n{prompt}"
#         )
#         response = model.generate_content(full_prompt)
#         return response.text.strip()

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Load Gemini 2.0 Flash model
model = genai.GenerativeModel("models/gemini-2.0-flash")

class RiskPredictionAgent:
    def run(self, prompt: str, context: str) -> str:
        role_prompt = (
            "You are a Risk Estimator Agent in a clinical reasoning system.\n"
            "Your job is to evaluate the patient's risk of relapse or worsening symptoms.\n"
            "Start by explaining the main risk factors you considered (reasoning), and then give a risk level summary (e.g., Low / Moderate / High).\n\n"
            f"Patient Context:\n{context}\n\n"
            f"Prompt:\n{prompt}\n\n"
            "Answer (reasoning followed by risk summary):"
        )
        response = model.generate_content(role_prompt)
        return response.text.strip()
