import io
from pathlib import Path
from typing import Any

from app.core.config import settings
from app.services.llm_explainer import llm_explainer

# Alae's new AI modules
try:
    from ai.document_verifier.preprocessing import preprocess_image
    from ai.document_verifier.ocr import extract_text, extract_data_fields
    from ai.document_verifier.parser import DocumentParser
    from ai.document_verifier.shap_explainer import DocumentExplainer
    ALAE_AI_AVAILABLE = True
except ImportError:
    ALAE_AI_AVAILABLE = False

try:
    import numpy as np
    from PIL import Image

    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    np = None  # type: ignore
    Image = None  # type: ignore

try:
    import torch
    import torch.nn as nn
    from torchvision import models, transforms

    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False


class DocumentVerifierService:
    def __init__(self):
        self.model = None
        self.transform = None
        self.device = "cpu"
        if TORCH_AVAILABLE:
            self._load_model()

    def _load_model(self):
        # Synchronized with Alae's main.py (ResNet50 + custom head)
        weights_path = settings.model_path / "best_model.pt"
        self.transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            ]
        )
        
        backbone = models.resnet50(weights=None)
        in_f = backbone.fc.in_features
        
        # Exact architecture from Alae's main.py
        backbone.fc = nn.Sequential(
            nn.Linear(in_f, 512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 2), # NUM_CLASSES = 2
        )

        if weights_path.exists():
            try:
                ckpt = torch.load(weights_path, map_location=self.device)
                # Check if it's a full checkpoint or just state_dict
                state_dict = ckpt["model_state"] if isinstance(ckpt, dict) and "model_state" in ckpt else ckpt
                backbone.load_state_dict(state_dict)
                print(f"Loaded Alae's ResNet50 model from {weights_path}")
            except Exception as e:
                print(f"Error loading weights: {e}. Running with uninitialized weights.")
        
        backbone.eval()
        self.model = backbone

    def _image_heuristics(self, img: Image.Image) -> tuple[float, list[str]]:
        anomalies: list[str] = []
        arr = np.array(img.convert("RGB"))
        score = 0.12

        w, h = img.size
        if w < 400 or h < 400:
            anomalies.append("Low resolution — possible screenshot or crop")
            score += 0.2

        std = float(arr.std())
        if std < 25:
            anomalies.append("Unusually flat color distribution")
            score += 0.15

        mean = arr.mean(axis=(0, 1))
        if mean.max() - mean.min() < 15:
            anomalies.append("Low color variance — possible template forgery")
            score += 0.1

        return min(0.98, score), anomalies

    def predict(self, file_bytes: bytes, filename: str = "upload.jpg") -> dict[str, Any]:
        if not PIL_AVAILABLE:
            return {
                "agent": "document_verifier",
                "verdict": "AUTHENTIC",
                "confidence": 0.75,
                "explanation": llm_explainer.explain_document("AUTHENTIC", 0.25, []),
                "anomalies": [],
                "technical_details": {"note": "Install Pillow for full image analysis: pip install Pillow"},
            }

        img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
        anomalies: list[str] = []
        ocr_text = ""
        doc_type = "UNKNOWN"

        # 1. Alae's AI Pipeline: OCR and Parsing
        if ALAE_AI_AVAILABLE:
            ocr_text = extract_text(file_bytes)
            doc_type = DocumentParser.identify_document_type(ocr_text)
            text_anomalies = DocumentParser.check_for_inconsistencies(ocr_text)
            anomalies.extend(text_anomalies)

        # 2. CNN Analysis (ResNet)
        if self.model is not None and TORCH_AVAILABLE:
            # Preprocess image using Alae's new preprocessing
            if ALAE_AI_AVAILABLE:
                processed_img = preprocess_image(img)
                # Apply normalization even with Alae's preprocessing
                tensor = transforms.Compose([
                    transforms.ToTensor(),
                    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                ])(processed_img).unsqueeze(0).to(self.device)
            else:
                tensor = self.transform(img).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                logits = self.model(tensor)
                proba = torch.softmax(logits, dim=1)[0]
                score_normal = round(proba[0].item(), 4)
                fake_score = round(proba[1].item(), 4) # score_anomaly
            
            weights_path = settings.model_path / "best_model.pt"
            if not weights_path.exists():
                heuristic_score, h_anomalies = self._image_heuristics(img)
                # Blend heuristic with model if model is untrained
                fake_score = (fake_score + heuristic_score) / 2
                anomalies.extend(h_anomalies)
        else:
            fake_score, h_anomalies = self._image_heuristics(img)
            score_normal = 1 - fake_score
            anomalies.extend(h_anomalies)

        # 3. Final Verdict and Explanation
        # Using Alae's threshold: SEUIL = 0.60
        ALAE_THRESHOLD = 0.60
        verdict = "FAKE" if fake_score >= ALAE_THRESHOLD else "AUTHENTIC"
        
        # Add OCR insights to explanation
        if doc_type != "UNKNOWN":
            anomalies.append(f"Document identified as {doc_type}")

        explanation = llm_explainer.explain_document(
            verdict, fake_score if verdict == "FAKE" else score_normal, anomalies
        )

        return {
            "agent": "document_verifier",
            "verdict": verdict,
            "confidence": round(fake_score if verdict == "FAKE" else score_normal, 4),
            "explanation": explanation,
            "anomalies": list(set(anomalies)),  # Unique anomalies
            "technical_details": {
                "filename": filename,
                "document_type": doc_type,
                "ocr_preview": ocr_text[:100] + "..." if len(ocr_text) > 100 else ocr_text,
                "size": list(img.size),
                "score_normal": score_normal,
                "score_anomaly": fake_score,
                "seuil": ALAE_THRESHOLD,
            },
        }


document_service = DocumentVerifierService()
