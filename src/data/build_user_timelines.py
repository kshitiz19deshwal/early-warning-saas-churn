import pandas as pd
import glob
import os

RAW_EVENTS_DIR = "data/raw/saas_events"
OUTPUT_DIR = "data/processed"

def load_all_events():
    files = glob.glob(f"{RAW_EVENTS_DIR}/*.csv")
    df_list = [pd.read_csv(file) for file in files]
    return pd.concat(df_list, ignore_index=True)

def build_user_timelines(df):
    timeline = df.groupby("user_id").agg(
        total_logins=("event_type", lambda x: (x == "login").sum()),
        total_feature_uses=("event_type", lambda x: (x == "feature_use").sum()),
        avg_session_minutes=("session_minutes", "mean"),
        payment_failures=("payment_status", lambda x: (x == "failed").sum()),
        plan_type=("plan_type", "last"),
        churn_label=("churn_label", "max")
    ).reset_index()

    return timeline

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = load_all_events()
    timeline_df = build_user_timelines(df)

    output_path = f"{OUTPUT_DIR}/user_behavior_timeline.csv"
    timeline_df.to_csv(output_path, index=False)

    print("✅ User behavior timelines created")
    print(f"📁 Saved to {output_path}")

if __name__ == "__main__":
    main()
