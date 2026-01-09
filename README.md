# 🧬 Hybrid Healthcare AI Agent

**Clinical Health Risk Assessment & Decision Support System**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Overview

The **Hybrid Healthcare AI Agent** is an end-to-end machine learning application designed to assess cardiometabolic health risk based on lifestyle and clinical parameters. This portfolio project demonstrates the integration of traditional ML with modern Generative AI to create a reliable, explainable healthcare decision support system.

### The Hybrid Approach

The system combines three complementary AI paradigms:

1. **Traditional ML** (Random Forest) for accurate risk prediction
2. **Generative AI** (Google Gemini LLM) for personalized clinical explanations
3. **Rule-based logic** as a safe fallback mechanism when LLM is unavailable

This hybrid architecture ensures **reliability**, **explainability**, and **fault tolerance** — critical requirements for healthcare and pharmaceutical applications.

> ⚠️ **Disclaimer**: This project is intended for educational and research purposes only. It is NOT intended for real-world medical diagnosis or treatment decisions.

---

## 🎯 Key Features

✅ **Multi-level health risk classification**: Low / Medium / High  
✅ **Explainable AI** with clinical-style natural language explanations  
✅ **Fault-tolerant LLM integration** with graceful fallback to rule-based system  
✅ **Clean modular architecture** following functional programming principles  
✅ **Interactive Streamlit UI** with real-time predictions  
✅ **Probability distributions** for transparent decision-making  
✅ **Feature importance analysis** for model interpretability  
✅ **Personalized recommendations** for diet and exercise plans  

---

## 🏗️ System Architecture

```
┌─────────────────────┐
│   User Input (UI)   │
│   (Streamlit Form)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Feature Encoding    │
│ (Label Encoders)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────┐
│  ML Model (Random Forest)   │
│  • Trained on clinical data │
│  • Outputs: Low/Med/High    │
│  • Confidence scores        │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   Risk Classification       │
│   + Probability Scores      │
└──────────┬──────────────────┘
           │
           ▼
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌─────────┐   ┌──────────────────┐
│ Gemini  │   │ Rule-Based       │
│ LLM     │   │ Fallback         │
│         │   │ (if LLM fails)   │
└────┬────┘   └────────┬─────────┘
     │                 │
     └────────┬────────┘
              ▼
┌──────────────────────────────┐
│  Personalized Explanation    │
│  + Clinical Recommendations  │
└──────────────────────────────┘
```

**Why This Architecture?**

- **ML ensures accuracy** through data-driven pattern recognition
- **LLM ensures clarity** through natural, empathetic communication
- **Rule-based fallback ensures reliability** when external APIs fail
- **Together they create trust** through transparent, understandable AI

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **ML Framework** | Scikit-learn (Random Forest) | Health risk prediction |
| **LLM** | Google Gemini | Natural language explanations |
| **Data Processing** | Pandas, NumPy | Feature engineering & cleaning |
| **Web Framework** | Streamlit | Interactive user interface |
| **Model Persistence** | Joblib | Save/load trained models |
| **Language** | Python 3.8+ | Core development |

---

## 📊 Dataset

**Source**: [Kaggle - Personalized Healthcare Recommendation System](https://www.kaggle.com/datasets/nailasrivastava/personalised-healthcare-recommendation-system)

### Clinical Features

| Feature | Type | Description | Range/Values |
|---------|------|-------------|--------------|
| `Age` | Numerical | Patient age in years | 18-100 |
| `BMI` | Numerical | Body Mass Index | 15.0-50.0 |
| `Glucose_Level` | Numerical | Fasting blood glucose (mg/dL) | 70-200 |
| `HbA1c` | Numerical | Hemoglobin A1c percentage | 4.0-12.0 |
| `Cholesterol` | Numerical | Total cholesterol (mg/dL) | 100-350 |
| `Smoking_Status` | Categorical | Never / Former / Current | 3 categories |
| `Physical_Activity_Level` | Categorical | Sedentary / Moderate / Active | 3 categories |
| `Alcohol_Consumption` | Categorical | None / Moderate / Heavy | 3 categories |

### Target Variable

- **`Health_Risk`**: Low / Medium / High (multiclass classification)

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Hugging face API Key

### Step-by-Step Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/hybrid-healthcare-ai.git
cd hybrid-healthcare-ai
```

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `pandas` - Data manipulation
- `scikit-learn` - ML modeling
- `streamlit` - Web UI
- `joblib` - Model serialization
- `google-generativeai` - Gemini LLM integration
- `numpy` - Numerical operations

#### 3️⃣ Download the Dataset

1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/nailasrivastava/personalised-healthcare-recommendation-system)
2. Download `personalised_dataset.csv`
3. Place it in the project root directory

#### 4️⃣ Preprocess Data

```bash
python data_pipeline.py
```

**What this does:**
- Loads the raw CSV data
- Handles missing values in `Alcohol_Consumption` column
- Encodes categorical features (Smoking, Activity Level, Alcohol)
- Splits data into 80% training / 20% testing sets
- Displays data statistics

#### 5️⃣ Train the ML Model

```bash
python model_trainer.py
```

**Expected Output:**
```
Training Random Forest model...
Model training complete!

==================================================
MODEL EVALUATION RESULTS
==================================================

Accuracy: 0.XXXX

Classification Report:
              precision    recall  f1-score   support
        Low       0.XX      0.XX      0.XX       XXX
     Medium       0.XX      0.XX      0.XX       XXX
       High       0.XX      0.XX      0.XX       XXX

==================================================
FEATURE IMPORTANCE ANALYSIS
==================================================
HbA1c                         : 0.XXXX
Glucose_Level                 : 0.XXXX
Cholesterol                   : 0.XXXX
...

Model saved successfully to 'health_model.joblib'
Metadata saved successfully to 'model_metadata.joblib'
```

This generates:
- `health_model.joblib` - Trained Random Forest classifier
- `model_metadata.joblib` - Feature names and label encoders

#### 6️⃣ Launch the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

### 🔐 Hugging Face API Configuration
Getting Your API Key
Visit Hugging Face
Sign in with your Hugging Face account
Click "New token" and select Read access
Copy the key (format: hf_xxx...)
Keep it secure and never commit it to version control


## 🎨 Using the Application

### User Interface Overview

The application features a clean, two-column layout:

**Left Column - Patient Information:**
- Age slider (18-100 years)
- BMI slider (15.0-50.0)
- Glucose Level slider (70-200 mg/dL)
- HbA1c slider (4.0-12.0%)
- Cholesterol slider (100-350 mg/dL)

**Right Column - Lifestyle Factors:**
- Smoking Status dropdown
- Physical Activity Level dropdown
- Alcohol Consumption dropdown

**Sidebar - Configuration:**
- System information
- About section

### Workflow

1. **Enter Patient Data**: Adjust sliders and dropdowns to match patient metrics
2. **Click "Analyze Health Risk"**: Triggers ML prediction
3. **View Results**:
   - **Risk Level**: Color-coded (Green=Low, Yellow=Medium, Red=High)
   - **Probability Distribution**: Visual bars showing confidence across all risk categories
   - **Recommendations**: Rule-based diet and exercise suggestions
   - **AI Explanation**: Personalized, empathetic 3-sentence summary from Gemini

### Example Output

```
Health Risk Level: Medium

Risk Probability Distribution:
Low:    15% ███
Medium: 68% █████████████████
High:   17% ████

Diet Plan: Low sugar, high fiber diet
Exercise Plan: 45 minutes moderate exercise 5x/week

AI Explanation:
Your current health metrics indicate a moderate risk level, primarily 
driven by elevated glucose and HbA1c levels that suggest potential 
prediabetes. The good news is that with consistent lifestyle modifications—
particularly following the recommended low-sugar, high-fiber diet and 
maintaining 45 minutes of moderate exercise five times weekly—you can 
significantly improve these markers and reduce your risk. You're taking 
an important step by monitoring your health, and these changes can make 
a real difference in preventing progression to higher risk categories.
```

---

## 🧠 Technical Deep Dive

### Machine Learning Pipeline

#### Algorithm Selection: Random Forest

**Why Random Forest?**

- ✅ Handles non-linear relationships in clinical data
- ✅ Resistant to overfitting (ensemble method)
- ✅ Provides feature importance for interpretability
- ✅ Works well with mixed data types (numerical + categorical)
- ✅ No need for feature scaling
- ✅ Robust to outliers

#### Training Process

1. **Data Loading**: Read CSV with pandas
2. **Cleaning**: Handle missing values (forward fill for Alcohol_Consumption)
3. **Encoding**: Transform categorical features using LabelEncoder
4. **Splitting**: 80/20 train-test split with stratification
5. **Training**: Fit Random Forest on training data
6. **Evaluation**: Assess on held-out test set
7. **Export**: Save model and metadata with joblib

#### Expected Performance

```
Accuracy: 85-92% (typical range)
Precision: 0.80-0.90 per class
Recall: 0.80-0.88 per class
F1-Score: 0.82-0.89 per class
```

**Most Important Features** (typical ranking):
1. HbA1c
2. Glucose_Level
3. Age
4. BMI
5. Cholesterol

``

## 🛡️ AI Safety & Ethical Considerations

### Safety Mechanisms

1. **Medical Disclaimer**: Prominent warning that this is educational, not diagnostic
2. **Transparent Predictions**: Shows probability distribution, not just final class
3. **Explainability**: Provides reasoning through LLM explanations
4. **Privacy**: No data storage; all processing is session-based
5. **Fallback System**: Rule-based logic if LLM fails
6. **Human Oversight**: Designed to assist, not replace healthcare professionals

### Limitations

- **Not FDA-approved**: This is a research/educational tool
- **Limited training data**: Model only as good as the dataset
- **No personalized medical history**: Cannot account for individual context
- **Requires validation**: Should be validated on diverse populations before any clinical consideration

### Best Practices

✅ Always include medical disclaimers  
✅ Make predictions transparent (show probabilities)  
✅ Provide explanations, not just predictions  
✅ Implement fallback mechanisms for reliability  
✅ Test thoroughly on edge cases  
✅ Never claim diagnostic accuracy  

---

## 📈 Model Performance Metrics

### Classification Report (Example)

```
              precision    recall  f1-score   support

         Low       0.88      0.91      0.89       245
      Medium       0.85      0.83      0.84       198
        High       0.89      0.87      0.88       157

    accuracy                           0.87       600
   macro avg       0.87      0.87      0.87       600
weighted avg       0.87      0.87      0.87       600
```

### Feature Importance

```
HbA1c                    : 0.2847
Glucose_Level            : 0.2315
Age                      : 0.1523
BMI                      : 0.1198
Cholesterol              : 0.0982
Smoking_Status           : 0.0645
Physical_Activity_Level  : 0.0490
```

**Interpretation**: HbA1c and Glucose are the strongest predictors of health risk, which aligns with clinical knowledge about diabetes and cardiometabolic disease.

---

## 🚧 Future Enhancements

### Short-term Roadmap

- [ ] Add confusion matrix visualization to UI
- [ ] Implement SHAP values for individual prediction explanations
- [ ] Add data validation and input sanitization
- [ ] Create unit tests for all modules
- [ ] Add logging for debugging and monitoring

### Medium-term Roadmap

- [ ] Integrate additional ML models (XGBoost, LightGBM) for comparison
- [ ] Add time-series tracking for patient progress
- [ ] Implement multi-language support for global accessibility
- [ ] Deploy to Streamlit Cloud / Hugging Face Spaces
- [ ] Add PDF export of health reports

### Long-term Vision

- [ ] Integration with wearable device APIs (Fitbit, Apple Health)
- [ ] Conversational AI chatbot for follow-up questions
- [ ] Multi-modal input (accept lab reports as images/PDFs)
- [ ] Federated learning for privacy-preserving model updates
- [ ] Clinical trial partnership for real-world validation

---

## 🤝 Contributing

This is a portfolio project, but contributions and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🙏 Acknowledgments

- **Dataset**: Naila Srivastava ([Kaggle](https://www.kaggle.com/datasets/nailasrivastava/personalised-healthcare-recommendation-system))
- **ML Framework**: Scikit-Learn Development Team
- **LLM**: Google Gemini / DeepMind
- **UI Framework**: Streamlit
- **Community**: Stack Overflow, Kaggle, Hugging Face

---

## 👨‍💻 Author

**Sri Nithya S**

- 🔗 LinkedIn: [your-linkedin-profile](https://www.linkedin.com/in/sri-nithya-s-0b47681a4/
)
---

## 📞 Contact & Support

Have questions or suggestions? Feel free to:

- 🐛 Open an issue on GitHub
- 💬 Connect on LinkedIn

---
