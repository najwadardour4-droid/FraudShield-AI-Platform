import io
from typing import Optional

try:
    import pytesseract
    PYTESSERACT_AVAILABLE = True
except ImportError:
    PYTESSERACT_AVAILABLE = False

def extract_text(image_bytes: bytes) -> str:
    """
    Extract text from document image using OCR.
    """
    if not PYTESSERACT_AVAILABLE:
        return "[OCR Error: pytesseract not installed. Please install it and the Tesseract engine.]"
    
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))
    
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"[OCR Error: {str(e)}]"

def extract_data_fields(text: str) -> dict:
    """
    Heuristic-based extraction of key fields like amounts or dates.
    """
    data = {}
    # Simple example: look for currency patterns
    import re
    amounts = re.findall(r"(\d+[\.,]\d{2})\s*(?:€|EUR|MAD|DH)", text)
    if amounts:
        data["detected_amounts"] = amounts
        
    dates = re.findall(r"(\d{2}/\d{2}/\d{4})", text)
    if dates:
        data["detected_dates"] = dates
        
    return data
