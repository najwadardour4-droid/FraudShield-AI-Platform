"""
Train a synthetic XGBoost credit-card fraud model for demo/PFE.
Run from backend/: python -m ai.train_credit_card
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

FEATURES = ["amount", "hour_of_day", "distance_from_home_km", "v1", "v2", "v3"]
OUT = Path(__file__).resolve().parents[1] / "ml_models" / "xgboost_model.pkl"
LEGACY = Path(__file__).resolve().parents[1] / "app" / "models" / "xgboost_model.pkl"


def generate_synthetic(n: int = 5000) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    df = pd.DataFrame(
        {
            "amount": rng.exponential(500, n),
            "hour_of_day": rng.integers(0, 24, n),
            "distance_from_home_km": rng.exponential(30, n),
            "v1": rng.normal(0, 1, n),
            "v2": rng.normal(0, 1, n),
            "v3": rng.normal(0, 1, n),
        }
    )
    risk = (
        (df["amount"] > 3000).astype(float) * 0.4
        + (df["hour_of_day"] < 5).astype(float) * 0.3
        + (df["distance_from_home_km"] > 150).astype(float) * 0.35
        + rng.random(n) * 0.1
    )
    df["is_fraud"] = (risk > 0.55).astype(int)
    return df


def main():
    df = generate_synthetic()
    X = df[FEATURES]
    y = df["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBClassifier(
        n_estimators=80,
        max_depth=4,
        learning_rate=0.1,
        eval_metric="logloss",
        random_state=42,
    )
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, OUT)
    joblib.dump(model, LEGACY)
    print(f"Saved model to {OUT} (test accuracy: {acc:.2%})")


if __name__ == "__main__":
    main()
