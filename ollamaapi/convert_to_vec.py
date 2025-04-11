import requests
import json

def get_embedding(text, model="nomic-embed-text:latest"):
    url = "http://localhost:11434/api/embeddings"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": text
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("embedding")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None


if __name__ == "__main__":
    sample_text = "Ollama makes it easy to run large language models locally."
    vector = get_embedding(sample_text)
