import re
import string
from pathlib import Path
from typing import Any

import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from app.core.config import settings
from app.services.llm_explainer import llm_explainer

# Configure local NLTK data path to avoid PermissionError
BASE_DIR = Path(__file__).resolve().parent.parent.parent
NLTK_DATA_PATH = str(BASE_DIR / "nltk_data")
nltk.data.path.append(NLTK_DATA_PATH)

# Ensure NLTK data is downloaded locally
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('stopwords', download_dir=NLTK_DATA_PATH)
    nltk.download('punkt_tab', download_dir=NLTK_DATA_PATH)

PHISHING_KEYWORDS = [
    "urgent", "verify", "password", "click here", "limited time",
    "suspended", "wire transfer", "bitcoin", "gift card",
    "confirm your account", "unusual activity", "free money",
    "lottery", "inheritance", "act now",
]

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text: str) -> str:
        # 1. Remove URLs
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        # 2. Convert to lowercase
        text = text.lower()
        # 3. Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # 4. Tokenization and Stopwords removal
        tokens = word_tokenize(text)
        cleaned_tokens = [w for w in tokens if w not in self.stop_words]
        return " ".join(cleaned_tokens)

class PhishingService:
    def __init__(self):
        self.pipeline = None
        self.preprocessor = TextPreprocessor()
        model_path = settings.model_path / "phishing_model.joblib"
        if model_path.exists():
            try:
                self.pipeline = joblib.load(model_path)
            except Exception as e:
                print(f"Error loading phishing model: {e}")

    def _keyword_signals(self, text: str) -> list[str]:
        lower = text.lower()
        return [kw for kw in PHISHING_KEYWORDS if kw in lower]

    def _heuristic_score(self, text: str) -> float:
        signals = self._keyword_signals(text)
        score = min(0.95, 0.1 + 0.12 * len(signals))
        if re.search(r"https?://[^\s]+", text, re.I):
            score += 0.15
        if re.search(r"\b\d{4,}\b", text):
            score += 0.05
        return min(0.99, score)

    def predict(self, text: str, channel: str = "email") -> dict[str, Any]:
        # Preprocess text as per project requirements
        cleaned_text = self.preprocessor.clean_text(text)
        
        if self.pipeline is not None:
            try:
                # Assuming the pipeline includes the vectorizer (TF-IDF)
                proba = self.pipeline.predict_proba([cleaned_text])[0]
                classes = list(self.pipeline.classes_)
                # Usually 1 is SPAM/PHISHING, 0 is HAM/SAFE
                phishing_idx = classes.index(1) if 1 in classes else int(proba.argmax())
                risk = float(proba[phishing_idx])
            except Exception as e:
                print(f"Prediction error: {e}")
                risk = self._heuristic_score(text)
        else:
            risk = self._heuristic_score(text)

        signals = self._keyword_signals(text)
        verdict = "PHISHING" if risk >= settings.FRAUD_THRESHOLD else "SAFE"
        
        # Calculate confidence based on verdict
        confidence = risk if verdict == "PHISHING" else 1 - risk
        
        explanation = llm_explainer.explain_phishing(
            verdict, confidence, signals
        )

        return {
            "agent": "phishing_scanner",
            "verdict": verdict,
            "confidence": round(confidence, 4),
            "explanation": explanation,
            "technical_details": {
                "channel": channel,
                "matched_signals": signals,
                "risk_score": round(risk, 4),
                "preprocessed_text": cleaned_text[:100] + "..." if len(cleaned_text) > 100 else cleaned_text
            },
        }

phishing_service = PhishingService()
