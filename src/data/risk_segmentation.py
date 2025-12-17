import pandas as pd

INPUT_PATH = "data/processed/user_behavior_with_drift.csv"
OUTPUT_PATH = "data/processed/user_behavior_with_risk.csv"

def assign_risk_stage(drift_score):
    if drift_score < 0.3:
        return "Low"
    elif drift_score < 0.6:
        return "Medium"
    else:
        return "High"

def main():
    df = pd.read_csv(INPUT_PATH)

    df["risk_stage"] = df["behavioral_drift_score"].apply(assign_risk_stage)

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Risk stages assigned")
    print(f"📁 Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
