import requests
import json

def genCompletion(model:str, prompt:str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    Fulltext = ""
    with requests.post(url, json=payload, stream=True) as response:
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            exit(1)
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode('utf-8'))
                resp = chunk.get("response", "")

                Fulltext += resp
                # print(resp)
                print(resp, end='', flush=True)
    return Fulltext

if __name__ == "__main__":
    model = "llama3.2:3b"
    prompt = "Hello would na ja"
    fulltext = genCompletion(model, prompt)

