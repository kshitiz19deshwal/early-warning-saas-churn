import pandas as pd

INPUT_PATH = "data/processed/user_behavior_with_risk.csv"
OUTPUT_PATH = "data/processed/final_churn_output.csv"

def recommend_action(row):
    if row["risk_stage"] == "High":
        if row["payment_failures"] > 0:
            return "Billing support outreach"
        elif row["total_feature_uses"] < 5:
            return "Feature onboarding & education"
        else:
            return "Retention discount offer"

    elif row["risk_stage"] == "Medium":
        return "Engagement reminder & product tips"

    else:
        return "No action needed"

def main():
    df = pd.read_csv(INPUT_PATH)

    df["recommended_action"] = df.apply(recommend_action, axis=1)

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Retention actions generated")
    print(f"📁 Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
