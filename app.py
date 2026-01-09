import streamlit as st
import pickle
import pandas as pd

from config import MODEL_PATH, ENCODER_PATH
from llm_config import generate_health_explanation
from clinical_rules import rule_based_explanation

st.set_page_config(
    page_title="Hybrid Healthcare AI Agent",
    page_icon="🫀",
    layout="wide"
)

# Load artifacts
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoders = pickle.load(f)

st.title("🧬 Hybrid Healthcare AI Agent")
st.caption("Clinical Decision Support System (Educational Use Only)")

# Sidebar
st.sidebar.title("👩‍⚕️ Developer")
st.sidebar.markdown("""
**Sri Nithya S**  
AI & Machine Learning Engineer  

🔗 [LinkedIn](https://www.linkedin.com/in/sri-nithya-s-0b47681a4/)  
💻 [GitHub](https://github.com/Srinithya1503)
""")

# Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100)
    bmi = st.number_input("BMI", 10.0, 50.0)
    glucose = st.number_input("Glucose Level (mg/dL)", 70.0, 250.0)
    hba1c = st.number_input("HbA1c (%)", 4.0, 14.0)

with col2:
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100.0, 350.0)
    smoking = st.selectbox("Smoking Status", ["Non-smoker", "Current smoker"])
    activity = st.selectbox(
        "Physical Activity Level",
        ["Sedentary", "Lightly Active", "Active"]
    )
    alcohol = st.selectbox(
        "Alcohol Consumption",
        ["None", "Low", "High"]
    )

def safe_encode(col, value):
    le = label_encoders[col]
    if value not in le.classes_:
        return le.transform([le.classes_[0]])[0]
    return le.transform([value])[0]

if st.button("🔍 Analyze Health Risk"):
    encoded = {
        "Age": age,
        "BMI": bmi,
        "Smoking_Status": safe_encode("Smoking_Status", smoking),
        "Physical_Activity_Level": safe_encode("Physical_Activity_Level", activity),
        "Alcohol_Consumption": safe_encode("Alcohol_Consumption", alcohol),
        "Glucose_Level": glucose,
        "HbA1c": hba1c,
        "Cholesterol": cholesterol
    }

    df = pd.DataFrame([encoded])
    prediction = model.predict(df)[0]

    st.subheader("📊 Risk Classification")
    st.success(f"Predicted Health Risk: **{prediction}**")

    prompt = f"""
Patient health risk is classified as {prediction}.
Explain what this means clinically and provide
lifestyle recommendations in simple language.
"""

    with st.spinner("Generating clinical explanation..."):
        explanation = generate_health_explanation(prompt)

    if explanation is None:
        explanation = rule_based_explanation(prediction)
        st.warning("⚠️ Explanation generated using clinical rules (LLM unavailable)")

    st.subheader("🧠 Clinical Explanation")
    st.info(explanation)
