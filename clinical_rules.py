def rule_based_explanation(risk: str) -> str:
    if risk == "Low":
        return (
            "Your health indicators are within recommended clinical ranges. "
            "This suggests a low short-term cardiometabolic risk. "
            "Maintaining your current lifestyle with regular physical activity, "
            "balanced nutrition, and routine health monitoring is advised."
        )

    if risk == "Moderate":
        return (
            "Some health parameters are approaching clinical thresholds. "
            "This indicates a moderate cardiometabolic risk. "
            "Lifestyle interventions such as increased physical activity, "
            "dietary improvements, weight management, and stress reduction "
            "can significantly reduce future disease risk."
        )

    if risk == "High":
        return (
            "Multiple cardiometabolic indicators exceed recommended limits, "
            "suggesting elevated health risk. "
            "Clinical evaluation, regular monitoring of glucose and lipid levels, "
            "and structured lifestyle modification are strongly recommended."
        )

    return "Unable to generate clinical explanation."
