import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.0-flash")

class RiskPredictionAgent:
    def run(self, prompt: str, context: str) -> str:
        full_prompt = (
            "You are a clinical risk evaluator. Based on the patient's data, assess their likelihood of relapse or symptom worsening.\n\n"
            f"Context:\n{context}\n\n"
            f"Prompt:\n{prompt}"
        )
        response = model.generate_content(full_prompt)
        return response.text.strip()
