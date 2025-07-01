from flask import Flask, request, jsonify
import datetime
import os
from openai import OpenAI
from pinecone import Pinecone
# from cpt_rag import query_cpt_pinecone
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Load environment variables or set directly
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", os.getenv("PINECONE_API_KEY"))
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "cpt-codes-embeddings-2")

openai_client = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

def get_embeddings(texts, model="text-embedding-3-small"):
    response = openai_client.embeddings.create(input=texts, model=model)
    embeddings = [item.embedding for item in response.data]
    return embeddings

def query_cpt_pinecone(case_description, top_k=5):
    # Step 1: Get embedding for the query
    query_embedding = get_embeddings([case_description])[0]
    # Step 2: Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        include_values=False
    )
    # Step 3: Format results
    matches = []
    for match in results['matches']:
        matches.append({
            "score": match['score'],
            "metadata": match['metadata']
        })
    return matches

@app.route('/case', methods=['POST'])
def case_summary_and_cpt():
    data = request.get_json()
    case_description = data.get('case_description')
    if not case_description:
        return jsonify({"error": "Missing 'case_description' in request"}), 400

    # Step 1: Summarize the case
    # summary = summarize_chain.invoke({"case": case_description})
    # print("--- summary complete", datetime.datetime.now())

    # Step 2: Retrieve CPT code(s)
    cpt_results = query_cpt_pinecone(case_description)
    print("--- retrieval complete", datetime.datetime.now())

    # Step 3: Format output
    formatted_cpt = []
    # cpt_results may be a list of Document objects
    for doc in cpt_results:
        formatted_cpt.append({
            "content": getattr(doc, 'page_content', str(doc)),
            "metadata": getattr(doc, 'metadata', {})
        })

    return jsonify({
        "summary": case_description,
        "cpt_results": formatted_cpt
    })

if __name__ == '__main__':
    app.run(debug=True) 