from flask import Flask, request, jsonify, send_file
from nlp_service import extract_entities
from ocr_service import extract_text_from_image
from transformers import pipeline
from fpdf import FPDF
from docx import Document
import os
from transformers import pipeline



app = Flask(__name__)

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization")
# Initialize Hugging Face text classification pipeline
# Initialize the Hugging Face zero-shot classification pipeline with the facebook/bart-large-mnli model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

@app.route('/')
def home():
    return "Welcome to the ERP Chatbot API!"

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    text = extract_text_from_image(file)
    return jsonify({"extracted_text": text})

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')
    summary = summarize_text_function(text)
    return jsonify({"summary": summary})

@app.route('/extract-entities', methods=['POST'])
def extract_entities_route():
    data = request.json
    text = data.get('text', '')
    entities = extract_entities(text)
    return jsonify({"entities": entities})

def summarize_text_function(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

@app.route('/classify-text', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')

    # Define your list of document types (labels)
    candidate_labels = ["invoice", "contract", "receipt", "report", "letter", "agreement", "memo"]

    # Perform zero-shot classification
    result = classifier(text, candidate_labels)

    # Get the label with the highest score
    classification = result['labels'][0]

    return jsonify({"classification": classification})

# Route to convert text to PDF
@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    data = request.json
    text = data.get('text', '')

    if text == '':
        return jsonify({"error": "No text to convert"}), 400

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    pdf_file = "converted_document.pdf"
    pdf.output(pdf_file)

    return send_file(pdf_file, as_attachment=True)

# Route to convert text to Word (DOCX)
@app.route('/convert-to-word', methods=['POST'])
def convert_to_word():
    data = request.json
    text = data.get('text', '')

    if text == '':
        return jsonify({"error": "No text to convert"}), 400

    doc = Document()
    doc.add_paragraph(text)

    word_file = "converted_document.docx"
    doc.save(word_file)

    return send_file(word_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
