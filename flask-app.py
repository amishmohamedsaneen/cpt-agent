from flask import Flask, request, jsonify
import datetime
import os
from pinecone import Pinecone
from dotenv import load_dotenv
from openaiWrapper import get_embeddings, gpt_summarize_and_categorize
from config import PINECONE_INDEX_NAME
import json
from cpt_EM_code.cpt_em_mdm import cpt_mdm_driver

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

    # Step 1: Summarize and categorize the case
    gpt_result = gpt_summarize_and_categorize(case_description)
    try:
        gpt_json = json.loads(gpt_result)
    except Exception:
        gpt_json = {"summary": case_description, "evaluation and management": "", "other": ""}

    # Step 2: If evaluation and management present, use cpt_mdm_driver
    eval_mgmt = gpt_json.get("evaluation and management", "")
    if eval_mgmt and str(eval_mgmt).strip().lower() not in ["", "none", "false", "no"]:
        mdm_data = {
            "summary": gpt_json.get("summary", case_description)
        }
        cpt_code, reason = cpt_mdm_driver(mdm_data)
        return jsonify({
            "summary": gpt_json.get("summary", case_description),
            "evaluation and management": eval_mgmt,
            "cpt_code": cpt_code,
            "reason": reason,
            "other": gpt_json.get("other", "")
        })

    # Step 3: Otherwise, retrieve CPT code(s) from Pinecone
    cpt_results = query_cpt_pinecone(case_description)
    print("--- retrieval complete", datetime.datetime.now())

    formatted_cpt = []
    for doc in cpt_results:
        formatted_cpt.append({
            "content": getattr(doc, 'page_content', str(doc)),
            "metadata": getattr(doc, 'metadata', {})
        })

    return jsonify({
        "summary": gpt_json.get("summary", case_description),
        "evaluation and management": eval_mgmt,
        "other": gpt_json.get("other", ""),
        "cpt_results": formatted_cpt
    })

if __name__ == '__main__':
    app.run(debug=True) 