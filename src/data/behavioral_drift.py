import pandas as pd
import os

INPUT_PATH = "data/processed/user_behavior_timeline.csv"
OUTPUT_PATH = "data/processed/user_behavior_with_drift.csv"

def calculate_behavioral_drift(df):
    df = df.copy()

    # Normalize key behavior metrics
    df["login_score"] = df["total_logins"] / df["total_logins"].max()
    df["feature_score"] = df["total_feature_uses"] / df["total_feature_uses"].max()
    df["session_score"] = df["avg_session_minutes"] / df["avg_session_minutes"].max()

    # Payment risk (higher failures = higher risk)
    df["payment_score"] = 1 - (df["payment_failures"] / (df["payment_failures"].max() + 1))

    # Combine into a single drift score
    df["behavioral_drift_score"] = (
        (1 - df["login_score"]) * 0.3 +
        (1 - df["feature_score"]) * 0.3 +
        (1 - df["session_score"]) * 0.2 +
        (1 - df["payment_score"]) * 0.2
    )

    return df

def main():
    df = pd.read_csv(INPUT_PATH)
    df = calculate_behavioral_drift(df)

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Behavioral drift calculated")
    print(f"📁 Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
