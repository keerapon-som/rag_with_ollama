import requests


def listAllModel():
    response = requests.get('http://localhost:11434/api/tags')
    for model in response.json()['models']:
        print(model['name'])

if __name__ == "__main__":       
    listAllModel()