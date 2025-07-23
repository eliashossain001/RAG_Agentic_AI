# import os
# from typing import Optional
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variable
# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure Gemini with the correct full model ID
# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel("models/gemini-2.0-flash")

# class DiagnosisAgent:
#     def run(self, prompt: str, context: str, image_path: Optional[str] = None) -> str:
#         full_prompt = (
#             "You are a clinical diagnosis assistant. Based on the following patient context, "
#             "provide a likely diagnosis. Consider both the context and any medical image provided.\n\n"
#             f"Context:\n{context}\n\n"
#             f"Prompt:\n{prompt}"
#         )

#         if image_path and os.path.exists(image_path):
#             with open(image_path, "rb") as img_file:
#                 image_data = img_file.read()

#             response = model.generate_content(
#                 [full_prompt, genai.types.Blob(mime_type="image/jpeg", data=image_data)]
#             )
#         else:
#             response = model.generate_content(full_prompt)

#         return response.text.strip()

import os
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variable
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini with the correct model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.0-flash")

class DiagnosisAgent:
    def run(self, prompt: str, context: str, image_path: Optional[str] = None) -> str:
        role_prompt = (
            "You are a medical diagnostician agent.\n"
            "Think step-by-step based on the patient's symptoms, history, and scan information.\n"
            "First explain your reasoning. Then provide the most likely diagnosis at the end.\n\n"
            f"Patient Context:\n{context}\n\n"
            f"Prompt:\n{prompt}\n\n"
            "Answer (step-by-step reasoning followed by final diagnosis):"
        )

        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                image_data = img_file.read()

            response = model.generate_content(
                [role_prompt, genai.types.Blob(mime_type="image/jpeg", data=image_data)]
            )
        else:
            response = model.generate_content(role_prompt)

        return response.text.strip()
