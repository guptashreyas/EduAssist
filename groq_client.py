# groq_client.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(prompt, model="openai/gpt-oss-20b"):
    """Send a prompt to Groq LLM and return its response."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are EduAssist, a friendly school learning chatbot."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
