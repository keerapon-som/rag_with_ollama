import requests
import json

def pull_model_stream(model_name):
    url = "http://localhost:11434/api/pull"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "stream": True  # Make sure streaming is enabled
    }

    # Stream the response
    with requests.post(url, headers=headers, json=data, stream=True) as response:
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return

        print("Pulling model...\n")
        for line in response.iter_lines():
            if line:
                try:
                    json_line = json.loads(line.decode("utf-8"))
                    print(json.dumps(json_line, indent=2))
                except json.JSONDecodeError as e:
                    print(f"Invalid JSON: {line}")


if __name__ == "__main__":
    pull_model_stream("nomic-embed-text:latest")
    