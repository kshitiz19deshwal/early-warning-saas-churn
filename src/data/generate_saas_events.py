import pandas as pd
import random
import os
from datetime import datetime

NUM_USERS = 200
EVENTS_PER_DAY = 500
OUTPUT_DIR = "data/raw/saas_events"

PLANS = ["free", "basic", "pro"]
FEATURES = ["dashboard", "analytics", "export", "automation"]

def generate_events_for_day(date):
    rows = []

    for _ in range(EVENTS_PER_DAY):
        user_id = f"user_{random.randint(1, NUM_USERS)}"
        plan_type = random.choices(PLANS, weights=[0.5, 0.3, 0.2])[0]

        event_type = random.choices(
            ["login", "feature_use", "payment"],
            weights=[0.5, 0.35, 0.15]
        )[0]

        session_minutes = 0
        feature_name = None
        payment_status = "none"

        if event_type == "login":
            session_minutes = random.randint(1, 60)

        elif event_type == "feature_use":
            feature_name = random.choice(FEATURES)
            session_minutes = random.randint(5, 90)

        elif event_type == "payment":
            payment_status = random.choices(
                ["success", "failed"],
                weights=[0.85, 0.15]
            )[0]

        churn_label = random.choices([0, 1], weights=[0.9, 0.1])[0]

        rows.append([
            user_id,
            date,
            event_type,
            session_minutes,
            feature_name,
            payment_status,
            plan_type,
            churn_label
        ])

    return pd.DataFrame(rows, columns=[
        "user_id",
        "event_date",
        "event_type",
        "session_minutes",
        "feature_name",
        "payment_status",
        "plan_type",
        "churn_label"
    ])

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = datetime.today().date()
    df = generate_events_for_day(today)
    path = f"{OUTPUT_DIR}/{today}.csv"
    df.to_csv(path, index=False)
    print(f"Generated SaaS events → {path}")

if __name__ == "__main__":
    main()
