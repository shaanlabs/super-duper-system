import requests

OLLAMA_URL = "http://localhost:11434/api/chat"  # Ollama API default

def ask_ollama(model: str, prompt: str) -> str:
    """
    Sends a chat message to the Ollama model and returns the reply text.
    """
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are Code Mentor, an expert programming tutor."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        # Improved error handling for missing/invalid response
        if "message" in data and "content" in data["message"]:
            return data["message"]["content"]
        else:
            return "⚠️ Error: Invalid response from Ollama."
    except requests.exceptions.Timeout:
        return "⚠️ Error: Ollama API request timed out."
    except Exception as e:
        return f"⚠️ Error communicating with Ollama: {e}"
