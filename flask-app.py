from flask import Flask, request, jsonify
import datetime
import os
from pinecone import Pinecone
# from cpt_rag import query_cpt_pinecone
from dotenv import load_dotenv
from openaiWrapper import get_embeddings
from config import PINECONE_INDEX_NAME

app = Flask(__name__)
load_dotenv()

# Load environment variables or set directly
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

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