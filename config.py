import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "text-embedding-3-small")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "cpt-codes-embeddings-2") 