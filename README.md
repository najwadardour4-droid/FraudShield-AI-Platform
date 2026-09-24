# 🛡️ FraudShield AI — Enterprise Fraud Intelligence Platform

## AI-Powered Fraud Detection & Explainable Intelligence System

FraudShield AI is an end-to-end fraud intelligence platform developed as a **2026 Final Year Project (PFE)**.

The platform combines **Machine Learning, Deep Learning, NLP, Explainable AI (XAI), and real-time web technologies** to detect and analyze different types of fraud.

The system includes a **FastAPI backend**, an **Angular frontend**, AI-based detection modules, and **WebSocket communication** for real-time updates.

---

## 🎯 Project Overview

Financial systems can face multiple types of threats, including:

- 💳 Credit card fraud
- 🎣 Phishing attacks
- 📄 Document forgery

FraudShield AI aims to provide an intelligent system capable of:

- Detecting suspicious activities
- Assigning a fraud risk score
- Explaining ML predictions using SHAP
- Monitoring AI agents in real time
- Displaying results through an interactive dashboard

---

## 👥 Multi-Agent Architecture

The project is organized into specialized AI modules:

| Agent | Responsibility | Technology |
|------|----------------|------------|
| Credit Card Investigator | Transaction fraud detection & risk scoring | XGBoost + SHAP |
| Phishing Scanner | Phishing and malicious content detection | NLP + LLM |
| Document Verifier | Document authenticity analysis | CNN / ResNet50 |

### My Contribution

I worked primarily on the **Credit Card Investigator** module.

My responsibilities included:

- Data preprocessing and feature engineering
- Machine Learning model development
- Fraud prediction using XGBoost
- Explainability using SHAP
- Risk score generation
- Backend/API integration
- Integration with the real-time dashboard

---

## 🧠 System Architecture

```text
User / Transaction Input
        ↓
Feature Engineering
        ↓
AI Detection Modules
(XGBoost / NLP / CNN)
        ↓
Prediction & Analysis
        ↓
SHAP Explainability
        ↓
Fraud Risk Score
        ↓
FastAPI Backend
        ↓
WebSocket Communication
        ↓
Angular Dashboard
```

---

## ⚙️ Backend

The backend was developed using **FastAPI and Python**.

### Main components

* REST API
* WebSocket communication
* AI model integration
* Asynchronous processing
* Data validation
* Fraud risk scoring
* SHAP explainability
* Structured logging

### Backend Technologies

* Python 3.11
* FastAPI
* XGBoost
* SHAP
* PyTorch
* WebSockets
* SQLite

---

## 💻 Frontend

The frontend provides an interactive dashboard for monitoring fraud detection results and AI agent activity.

### Main features

* Real-time fraud monitoring
* Fraud analytics dashboard
* AI agent activity monitoring
* Explainable AI visualization
* Live fraud event stream
* Interactive charts

### Frontend Technologies

* Angular 21
* TypeScript
* RxJS
* Angular Signals
* SCSS
* Chart.js / D3.js

---

## 🔄 Real-Time Detection Flow

1. A transaction is received by the system.
2. Input data is processed and transformed.
3. The XGBoost model predicts the probability of fraud.
4. SHAP identifies the main features influencing the prediction.
5. A risk score is generated.
6. The result is sent through the backend.
7. WebSocket communication updates the dashboard in real time.

---

## 📊 Key Features

* 💳 Credit card fraud detection
* 🤖 Multi-agent AI architecture
* 🧠 Machine Learning with XGBoost
* 🔍 Explainable AI with SHAP
* ⚡ Real-time WebSocket communication
* 📈 Interactive fraud analytics
* 🎣 Phishing detection module
* 📄 Document verification module
* 🖥️ Full-Stack web architecture

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* XGBoost
* SHAP
* PyTorch

### Frontend

* Angular
* TypeScript
* RxJS
* SCSS
* Chart.js / D3.js

### Data & Database

* Pandas
* NumPy
* SQLite
* SQL

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
fraud-detection-platform/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── models/
│   │   └── schemas/
│   │
│   ├── ai/
│   └── ml_models/
│
├── frontend/
│   └── src/
│       └── app/
│           ├── pages/
│           ├── services/
│           └── layout/
│
└── README.md
```

---

## 🎓 Academic Context

**Final Year Project (PFE) — 2026**

### Focus Areas

* Artificial Intelligence
* Machine Learning
* Explainable AI
* Cybersecurity
* Financial Fraud Detection
* Full-Stack Development
* Real-Time Web Applications

---

## 🚀 Skills Demonstrated

This project allowed me to work across several areas of software and AI development:

* Python development
* REST API development
* Full-Stack web development
* Machine Learning
* Data preprocessing
* Model integration
* Explainable AI
* Real-time communication
* Database integration
* Frontend development
* Git & GitHub

---

## 📌 Project Goal

FraudShield AI demonstrates how AI models can be integrated into a complete web application to support **fraud detection, analysis, explainability, and real-time monitoring**.

The project combines an AI layer with a modern Full-Stack architecture to create an end-to-end intelligent application.

---

## 👩‍💻 Author

**Najwa Dardour**

Licence in Data Analysis — FST Tangier

Main contribution:
**Credit Card Fraud Detection — XGBoost + SHAP**
