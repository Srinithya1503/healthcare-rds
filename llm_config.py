import requests
from config import HF_API_TOKEN

HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}


def generate_health_explanation(prompt: str):
    """
    Attempts to generate explanation using Hugging Face LLM.
    Returns None if LLM is unavailable.
    """

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.3,
            "do_sample": False
        }
    }

    try:
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()[0]["generated_text"]

        return None

    except Exception:
        return None
