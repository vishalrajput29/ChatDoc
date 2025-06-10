import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def load_documents(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            content = extract_text_from_pdf(os.path.join(folder_path, file))
        elif file.endswith(('.png', '.jpg', '.jpeg')):
            content = extract_text_from_image(os.path.join(folder_path, file))
        else:
            continue
        docs.append({"filename": file, "content": clean_text(content)})
    return docs
