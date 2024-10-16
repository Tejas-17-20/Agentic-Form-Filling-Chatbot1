# app/chatbot.py

from flask import Blueprint, request, jsonify
import json
import spacy  # Using spaCy for NLP

# Load the NLP model
nlp = spacy.load("en_core_web_sm")  # You may need to install the spaCy model

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Process the input with NLP
    doc = nlp(user_input)
    
    # Example of information extraction (you can expand this)
    extracted_info = extract_information(doc)

    # Respond back with the extracted information
    response = {
        'response': generate_response(extracted_info)
    }

    return jsonify(response)

def extract_information(doc):
    # A simple example of extracting named entities (customize as needed)
    extracted_info = {}
    for ent in doc.ents:
        extracted_info[ent.label_] = ent.text

    return extracted_info

def generate_response(info):
    # Create a response based on extracted information
    if 'PERSON' in info:
        return f"Hello {info['PERSON']}, how can I help you with your form?"
    else:
        return "I'm here to assist you with your form-filling. Please provide your details."
