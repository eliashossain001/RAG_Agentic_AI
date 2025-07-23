# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("models/gemini-2.0-flash")

# class RecommendationAgent:
#     def run(self, prompt: str, context: str) -> str:
#         full_prompt = (
#             "You are a clinical support system. Suggest next actions based on history, conversation, and scans.\n\n"
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

# Gemini model
model = genai.GenerativeModel("models/gemini-2.0-flash")

class RecommendationAgent:
    def run(self, prompt: str, context: str) -> str:
        role_prompt = (
            "You are a recommendation agent in a clinical decision-making system.\n"
            "Based on the patient's history, symptoms, and scan summaries, suggest next steps in diagnosis or treatment.\n"
            "First explain your rationale. Then provide 2–3 actionable recommendations.\n\n"
            f"Patient Context:\n{context}\n\n"
            f"Prompt:\n{prompt}\n\n"
            "Answer (reasoning followed by recommendations):"
        )
        response = model.generate_content(role_prompt)
        return response.text.strip()
