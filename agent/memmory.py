from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def get_memory():
    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=OpenAIEmbeddings()
    )
