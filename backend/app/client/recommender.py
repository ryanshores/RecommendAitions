import requests

from services.prompts import build_prompt, SYSTEM_PROMPT
from config import settings


def recommend(titles, user_profile):
    prompt = build_prompt(titles, user_profile)
    response = requests.post(settings.ollama.url, json={
            "model": "qwen2.5-coder:7b",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        })
    return response.json()["message"]["content"]