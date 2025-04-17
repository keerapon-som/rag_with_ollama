
import ollamaapi.convert_to_vec as vec
import ollamaapi.generate_completion as o
import repository.db as repo



prompt = "Following all of these documents"

initialAsk = "Did the finance is have some project about blockchain ? and if it have , so what's the date that the project started ?"



vector_initialAsk = vec.get_embedding(
    text=initialAsk,
    model="nomic-embed-text:latest"
)

listData = repo.searchClosestVector(vector_initialAsk, embedingModel="nomic-embed-text:latest", limit=5)
i = 0
for data in listData:
    i += 1
    prompt += f"\nDocument {i} : {data['document']}"

prompt += f"\n\nQuestion: {initialAsk}\nAnswer:"

model="llama3.2:3b"

o.genCompletion(model, prompt)

