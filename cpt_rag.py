import os
import datetime
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Load and index the CPT data only once (at module load)
loader = CSVLoader(
    "/Users/hplx/Documents/2024/discharge-summary/cpt_sections_descriptions.csv",
    encoding="utf-8",
    csv_args={'delimiter':','}
)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OllamaEmbeddings(model="llama3.1"))
retriever = vectorstore.as_retriever()

def get_cpt_results(case_description):
    """
    Given a case description, create an embedding, query the vectorstore, and return the results.
    """
    # The retriever expects a string query
    results = retriever.invoke(case_description)
    formatted_cpt = []
    for doc in results:
        formatted_cpt.append({
            "content": getattr(doc, 'page_content', str(doc)),
            "metadata": getattr(doc, 'metadata', {})
        })
    return formatted_cpt 