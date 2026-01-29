import requests

from backend.app.utils.prompts import build_prompt, SYSTEM_PROMPT
from backend.app.config import settings


def recommend(titles, user_profile):
    prompt = build_prompt(titles, user_profile)
    response = requests.post(settings.OLLAMA_URL, json={
            "model": "qwen2.5-coder:7b",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        })
    return response.json()["message"]["content"]