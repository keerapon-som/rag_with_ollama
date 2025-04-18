from repository import db as repo
from ollamaapi import convert_to_vec



data = "Is apple company have sustainability plan or not ?"
embedingModel = "nomic-embed-text:latest"
vector = convert_to_vec.get_embedding(
    text=data,
    model=embedingModel
)

listDocs = repo.searchClosestVector(vector, embedingModel=embedingModel, limit=5)
for data in listDocs:
    print(data["document"])