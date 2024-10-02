# backend/ocr_service.py

import pytesseract
from PIL import Image
import io

def extract_text_from_image(file):
    """Extract text from an uploaded image file using Tesseract OCR."""
    # Read the image file
    image = Image.open(file.stream)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text
