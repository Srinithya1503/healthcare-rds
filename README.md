🧬 Hybrid Healthcare AI Agent

Clinical Health Risk Assessment & Decision Support System

📌 Overview

The Hybrid Healthcare AI Agent is an end-to-end machine learning application designed to assess cardiometabolic health risk based on lifestyle and clinical parameters.

The system combines:

Traditional ML (Random Forest) for risk prediction

Open-source LLM (Hugging Face) for clinical explanations

Rule-based clinical logic as a safe fallback mechanism

This hybrid approach ensures reliability, explainability, and fault tolerance, making it suitable for healthcare and pharmaceutical applications.

⚠️ Educational use only. Not intended for medical diagnosis.

🎯 Key Features

✅ Health risk classification: Low / Moderate / High

✅ Explainable AI with clinical-style explanations

✅ Fault-tolerant LLM integration (graceful fallback)

✅ Clean modular architecture

✅ Streamlit-based interactive UI

✅ Open-source & cost-free inference stack

🏗️ System Architecture
User Input (UI)
      ↓
Feature Encoding
      ↓
ML Model (Random Forest)
      ↓
Risk Classification
      ↓
┌───────────────┐
│ Hugging Face  │  (if available)
│ LLM           │
└───────┬───────┘
        ↓
┌────────────────────────┐
│ Rule-Based Explanation │ (fallback)
└────────────────────────┘

📁 Project Structure
health-rmds/
│
├── app.py                  # Streamlit application
├── data_pipeline.py        # Data preprocessing & encoding
├── model_trainer.py        # ML model training
├── llm_config.py           # Hugging Face LLM integration
├── clinical_rules.py       # Rule-based fallback explanations
├── config.py               # Central configuration & secrets
├── personalised_dataset.xlsx
├── requirements.txt
└── README.md

⚙️ Tech Stack

Python 3.10+

Scikit-learn – ML modeling

Pandas / NumPy – Data processing

Streamlit – UI

Hugging Face Inference API – LLM explanations

Random Forest Classifier

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Preprocess data
python data_pipeline.py

3️⃣ Train model
python model_trainer.py

4️⃣ Launch app
streamlit run app.py

🔐 Configuration

Set your Hugging Face token in config.py:

HF_API_TOKEN = "hf_xxxxxxxxxxxxxxxxx"


In production, secrets should be stored using environment variables or a secrets manager.

🧠 AI Safety & Reliability

The application does not rely solely on LLMs

If the LLM is unavailable, the system automatically switches to a deterministic rule-based explanation

This ensures continuous availability and explainability, which is critical in healthcare systems

👩‍⚕️ Developer

Sri Nithya S
AI & Machine Learning Engineer

🔗 LinkedIn: https://www.linkedin.com/in/sri-nithya-s-0b47681a4/

💻 GitHub: https://github.com/Srinithya1503

📜 Disclaimer

This project is intended for educational and research purposes only and should not be used for real-world medical decision-making.