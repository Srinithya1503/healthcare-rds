import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from config import DATA_PATH, ENCODER_PATH

def main():
    df = pd.read_excel(DATA_PATH)

    categorical_cols = [
        "Smoking_Status",
        "Physical_Activity_Level",
        "Alcohol_Consumption"
    ]

    label_encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = df[col].fillna("Unknown")
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    numeric_cols = [
        "Age", "BMI", "Glucose_Level",
        "HbA1c", "Cholesterol"
    ]

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    with open(ENCODER_PATH, "wb") as f:
        pickle.dump(label_encoders, f)

    df.to_csv("processed_data.csv", index=False)
    print("✅ Data processing complete")

if __name__ == "__main__":
    main()
