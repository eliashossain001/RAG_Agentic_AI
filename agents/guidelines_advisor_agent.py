import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Use Gemini 2.0 Flash
model = genai.GenerativeModel("models/gemini-2.0-flash")

class GuidelinesAdvisorAgent:
    def run(self, prompt: str, context: str) -> str:
        full_prompt = (
            "You are a Guidelines Advisor Agent in a medical diagnostic system.\n"
            "Your role is to assess the patient context strictly using established medical guidelines and protocols.\n"
            "Refer to clinical standards (e.g., NICE, CDC, WHO) where relevant. Clearly state which guideline(s) support your reasoning.\n"
            "Provide reasoning followed by a conclusion aligned with protocols.\n\n"
            f"Patient Context:\n{context}\n\n"
            f"Prompt:\n{prompt}\n\n"
            "Answer:"
        )
        response = model.generate_content(full_prompt)
        return response.text.strip()
