"""
Train TF-IDF + Logistic Regression phishing classifier on sample messages.
Run from backend/: python -m ai.train_phishing
"""

from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

OUT = Path(__file__).resolve().parents[1] / "ml_models" / "phishing_model.joblib"

PHISHING = [
    "Urgent verify your bank account click here http://fake.com",
    "Your account suspended confirm password immediately",
    "You won lottery wire transfer fee act now",
    "Unusual activity detected login to secure portal",
    "Limited time offer free bitcoin investment",
    "Confirm your credentials or account will be closed",
    "Click here to update billing information",
    "IRS refund claim your gift card payment",
]
SAFE = [
    "Meeting rescheduled to tomorrow at 3pm in room B",
    "Please find attached the quarterly report for review",
    "Your order 48291 has shipped and will arrive Friday",
    "Reminder: team lunch on Thursday at the cafeteria",
    "Project kickoff notes from this morning's session",
    "Invoice 2024-118 approved by finance department",
    "Welcome to the platform here is your getting started guide",
    "Password policy updated please read the internal wiki",
]


def main():
    texts = PHISHING + SAFE
    labels = [1] * len(PHISHING) + [0] * len(SAFE)
    pipe = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=2000)),
            ("clf", LogisticRegression(max_iter=500)),
        ]
    )
    pipe.fit(texts, labels)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, OUT)
    print(f"Saved phishing model to {OUT}")


if __name__ == "__main__":
    main()
