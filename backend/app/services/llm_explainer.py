"""
Rule-based LLM-style explanation layer.
Produces human-readable narratives from model outputs (no external API required).
Replace with OpenAI/Ollama integration in production if needed.
"""

from typing import Any


class LLMExplainer:
    def explain_credit_card(
        self,
        verdict: str,
        confidence: float,
        features: dict[str, Any],
        shap_values: dict[str, float] | None = None,
    ) -> str:
        top = sorted((shap_values or {}).items(), key=lambda x: abs(x[1]), reverse=True)[:3]
        drivers = ", ".join(f"{k} ({'↑ risk' if v > 0 else '↓ risk'})" for k, v in top) if top else "transaction pattern"

        if verdict == "FRAUD":
            return (
                f"Najwa (Credit Card Investigator): This transaction is flagged as **fraudulent** "
                f"with {confidence:.0%} confidence. Primary risk drivers: {drivers}. "
                f"Recommend blocking the card and contacting the cardholder immediately."
            )
        return (
            f"Najwa (Credit Card Investigator): Transaction appears **legitimate** "
            f"({confidence:.0%} confidence). Observed features align with normal spending: {drivers}."
        )

    def explain_phishing(
        self,
        verdict: str,
        confidence: float,
        matched_signals: list[str],
    ) -> str:
        signals = ", ".join(matched_signals[:5]) if matched_signals else "no strong phishing patterns"
        if verdict == "PHISHING":
            return (
                f"Ferdaouss (Phishing Scanner): Message classified as **phishing** "
                f"({confidence:.0%} confidence). Detected signals: {signals}. "
                "Do not click links or share credentials."
            )
        return (
            f"Ferdaouss (Phishing Scanner): Message appears **safe** "
            f"({confidence:.0%} confidence). Reviewed signals: {signals}."
        )

    def explain_document(
        self,
        verdict: str,
        confidence: float,
        anomalies: list[str],
    ) -> str:
        issues = "; ".join(anomalies) if anomalies else "no major visual inconsistencies"
        if verdict == "FAKE":
            return (
                f"Alae (Document Verifier): Document likely **forged or manipulated** "
                f"({confidence:.0%} confidence). Anomalies: {issues}. "
                "Manual forensic review recommended."
            )
        return (
            f"Alae (Document Verifier): Document appears **authentic** "
            f"({confidence:.0%} confidence). Checks passed: {issues}."
        )


llm_explainer = LLMExplainer()
