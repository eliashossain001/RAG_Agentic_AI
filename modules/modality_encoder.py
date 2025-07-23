import base64
from PIL import Image
import io

def encode_mri_image(image_file) -> str:
    """
    Simulate modality embedding by summarizing image metadata.
    In a real system, you would pass this through a vision encoder.
    """
    try:
        image = Image.open(image_file)
        width, height = image.size
        mode = image.mode
        summary = f"MRI image uploaded ({mode} mode, {width}x{height} resolution)."
        return summary
    except Exception as e:
        return f"[Error reading image: {e}]"

def encode_text_file(text_file) -> str:
    """
    Read uploaded .txt file and decode into plain text.
    """
    try:
        return text_file.read().decode()
    except Exception as e:
        return f"[Error reading text file: {e}]"

def build_context(
    patient_id: str,
    medical_history: str,
    dialog: str,
    image_summary: str,
    pdf_data: str = ""
) -> str:
    """
    Combine all information into a formatted context string for the agents.
    Adds EHR/PDF content if available.
    """
    context = (
        f"Patient ID: {patient_id}\n\n"
        f"Medical History:\n{medical_history}\n\n"
        f"Doctor-Patient Dialog:\n{dialog}\n\n"
        f"Image Analysis:\n{image_summary}\n"
    )

    if pdf_data:
        context += f"\nEHR/Document Summary:\n{pdf_data.strip()}\n"

    return context
