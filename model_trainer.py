import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from config import MODEL_PATH

def main():
    df = pd.read_csv("processed_data.csv")

    features = [
        "Age", "BMI",
        "Smoking_Status",
        "Physical_Activity_Level",
        "Alcohol_Consumption",
        "Glucose_Level",
        "HbA1c",
        "Cholesterol"
    ]

    X = df[features]
    y = df["Health_Risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved")

if __name__ == "__main__":
    main()
