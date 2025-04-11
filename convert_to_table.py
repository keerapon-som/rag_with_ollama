from ollamaapi import convert_to_vec
from repository import db as repo
from util import file

documents = file.readJsonFile("./documentyimz.json")
embedingModel = "nomic-embed-text:latest"

listData = []

for doc in documents:

    vector_document = convert_to_vec.get_embedding(
        text=doc,
        model=embedingModel
    )

    data = {
        "document": doc,
        "vector_document": vector_document,
        "embed_model": embedingModel
    }

    listData.append(data)


repo.appendListData(listData)