import os
from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_embeddings(texts, model=MODEL_NAME):
    response = openai_client.embeddings.create(input=texts, model=model)
    embeddings = [item.embedding for item in response.data]
    return embeddings
