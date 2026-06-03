from fastapi import APIRouter, WebSocket
import asyncio
import json
import numpy as np
import datetime
import random

router = APIRouter(prefix="/ws", tags=["websocket"])

@router.websocket("/fraud-stream")
async def fraud_intelligence_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        processed_today = 18432
        while True:
            # Simulation of real-time fraud metrics
            probability = random.uniform(0.1, 0.98)
            risk_score = int(probability * 100)
            processed_today += random.randint(1, 3)
            
            # Simulated SHAP/XAI Drivers
            drivers = [
                {"name": "Transaction Amount", "impact": f"+{random.randint(25, 40)}%"},
                {"name": "Merchant Risk Score", "impact": f"+{random.randint(15, 30)}%"},
                {"name": "Unusual Geo Location", "impact": f"+{random.randint(10, 20)}%"}
            ]
            
            payload = {
                "system_time": datetime.datetime.now().strftime("%H:%M:%S"),
                "fraud_detection_accuracy": "99.96%",
                "model_confidence": f"{round(100 - (probability * 5), 2)}%",
                "processed_today": processed_today,
                "avg_inference": f"{random.randint(12, 16)}ms",
                "risk_criticality": "HIGH" if risk_score > 75 else ("MEDIUM" if risk_score > 40 else "LOW"),
                
                # Credit Card Agent Terminal Live Data (Najwa's Track)
                "credit_card_agent": {
                    "status": "ANALYZING" if risk_score > 40 else "IDLE",
                    "terminal_lines": [
                        "[MODEL] SHAP global feature impact computed... DONE",
                        f"[INPUT] Processing financial transaction batch #{random.randint(1000, 9999)}-X",
                        f"[OUTPUT] Risk Criticality Score: {risk_score}/100 -> {'FRAUD DETECTED' if risk_score > 75 else 'CLEARED'}"
                    ],
                    "xai_insights": {
                        "fraud_probability": f"{round(probability * 100, 1)}%",
                        "top_risk_drivers": drivers,
                        "decision": "High-risk fraudulent behavior detected." if risk_score > 75 else "Normal Activity monitored."
                    }
                },
                
                # Phishing Agent simulation
                "phishing_agent": {
                    "status": "SCANNING" if random.random() > 0.3 else "IDLE",
                    "terminal_lines": [
                        "[NLP] Tokenizing inbound email payloads... DONE",
                        f"[URL] Inspecting domain: secure-bank-{random.randint(100, 999)}.com",
                        f"[OUTPUT] Classification: {'PHISHING ATTEMPT' if random.random() > 0.8 else 'SAFE'}"
                    ]
                },
                
                # Document Agent simulation
                "document_agent": {
                    "status": "ACTIVE" if random.random() > 0.2 else "IDLE",
                    "terminal_lines": [
                        "[CV] ResNet50 tensor layer extraction... DONE",
                        f"[IMAGE] Analyzing metadata for document ID #{random.randint(10000, 99999)}",
                        f"[OUTPUT] Forgery Detection: {'ANOMALY FOUND' if random.random() > 0.9 else 'AUTHENTIC'}"
                    ]
                }
            }
            
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(2) # Update every 2 seconds
            
    except Exception as e:
        print(f"WebSocket connection closed: {e}")
    finally:
        try:
            await websocket.close()
        except:
            pass
