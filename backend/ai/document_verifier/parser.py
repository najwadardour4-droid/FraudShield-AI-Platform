from typing import Dict, Any
import re

class DocumentParser:
    """
    Parses OCR output to identify document types and potential red flags.
    """
    
    @staticmethod
    def identify_document_type(text: str) -> str:
        text_upper = text.upper()
        if any(keyword in text_upper for keyword in ["INVOICE", "FACTURE", "BILL"]):
            return "INVOICE"
        if any(keyword in text_upper for keyword in ["PASSPORT", "ID CARD", "CARTE D'IDENTITE"]):
            return "IDENTITY_DOCUMENT"
        if any(keyword in text_upper for keyword in ["RECEIPT", "TICKET"]):
            return "RECEIPT"
        return "UNKNOWN"

    @staticmethod
    def check_for_inconsistencies(text: str) -> list[str]:
        anomalies = []
        text_lower = text.lower()
        
        # Check for suspicious keywords often found in fake templates
        suspicious_keywords = ["sample", "template", "specimen", "void"]
        for kw in suspicious_keywords:
            if kw in text_lower:
                anomalies.append(f"Found suspicious keyword: '{kw}'")
                
        return anomalies
