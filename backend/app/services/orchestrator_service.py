from typing import Any

from app.services.credit_card_service import credit_card_service
from app.services.phishing_service import phishing_service


class OrchestratorService:
    """Central coordination layer — runs selected agents and aggregates risk."""

    def analyze(
        self,
        *,
        credit_card_payload: dict[str, Any] | None = None,
        phishing_text: str | None = None,
    ) -> dict[str, Any]:
        results: list[dict[str, Any]] = []

        if credit_card_payload:
            results.append(credit_card_service.predict(credit_card_payload))
        if phishing_text:
            results.append(phishing_service.predict(phishing_text))

        if not results:
            return {
                "summary": "No agents were selected for analysis.",
                "highest_risk_agent": None,
                "results": [],
            }

        flagged = [r for r in results if r["verdict"] in ("FRAUD", "PHISHING", "FAKE")]
        highest = max(results, key=lambda r: r["confidence"])

        if flagged:
            summary = (
                f"Orchestrator: {len(flagged)} agent(s) raised alerts. "
                f"Highest concern: {highest['agent']} ({highest['verdict']}, {highest['confidence']:.0%})."
            )
        else:
            summary = "Orchestrator: All analyzed inputs appear low risk."

        return {
            "summary": summary,
            "highest_risk_agent": highest["agent"] if flagged else None,
            "results": results,
        }


orchestrator_service = OrchestratorService()
