import numpy as np
from PIL import Image, ImageOps, ImageFilter

def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Apply preprocessing steps to enhance document for OCR and CNN.
    """
    # 1. Convert to Grayscale
    gray_image = image.convert("L")
    
    # 2. Enhance contrast
    enhanced_image = ImageOps.autocontrast(gray_image)
    
    # 3. Reduce noise
    denoised_image = enhanced_image.filter(ImageFilter.MedianFilter(size=3))
    
    # 4. Resize for CNN (ResNet expectation is usually 224x224)
    resized_image = denoised_image.resize((224, 224), Image.Resampling.LANCZOS)
    
    # 5. Convert back to RGB because ResNet expects 3 channels
    return resized_image.convert("RGB")

def detect_edges(image: Image.Image) -> Image.Image:
    """
    Detect edges to find potential document boundaries.
    """
    return image.filter(ImageFilter.FIND_EDGES)
