import requests
import json

def deleteModel(modelName:str):

    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "model": modelName
    }

    response = requests.delete('http://localhost:11434/api/delete', headers=headers, data=json.dumps(payload))
    print(response.text)


if __name__ == "__main__":        
    deleteModel("llama3.2:latest")