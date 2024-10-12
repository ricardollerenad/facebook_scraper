# Este archivo maneja la conexión a MongoDB y la subida de los datos:
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

def upload_to_mongodb(posts_data):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    result = collection.insert_many(posts_data)
    print(f"Inserted {len(result.inserted_ids)} posts into MongoDB")