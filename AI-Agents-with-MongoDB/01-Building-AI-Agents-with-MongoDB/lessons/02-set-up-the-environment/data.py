import key_param
from pymongo import MongoClient
import voyageai
from datasets import load_dataset

docs = load_dataset("MongoDB/mongodb-docs")
chunked_docs = load_dataset("MongoDB/mongodb-docs-embedded")

vo = voyageai.Client(api_key=key_param.voyage_api_key)

mongodb_client = MongoClient(key_param.mongodb_uri)

DB_NAME = "ai_agents"
FULL_COLLECTION_NAME = "full_docs"
VS_COLLECTION_NAME = "chunked_docs"
VS_INDEX_NAME = "vector_index"


db = mongodb_client[DB_NAME]
vs_collection = db[VS_COLLECTION_NAME]
full_collection = db[FULL_COLLECTION_NAME]

for doc in docs["train"]:
    full_collection.insert_one(doc)


for chunked_doc in chunked_docs["train"]:
    embedding = vo.embed(chunked_doc["body"], model="voyage-3-lite", input_type="document").embeddings[0]
    print(chunked_doc["body"])
    print(embedding)
    chunked_doc["embedding"] = embedding
    vs_collection.insert_one(chunked_doc)
    

model = {
    "name": VS_INDEX_NAME,
    "type": "vectorSearch",
    "definition": {
        "fields": [
            {
                "type": "vector",
                "path": "embedding",
                "numDimensions": 512,
                "similarity": "cosine",
            }
        ]
    },
}

vs_collection.create_search_index(model=model) 
