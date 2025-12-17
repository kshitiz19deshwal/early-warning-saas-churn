# Early-Warning SaaS Churn Prevention System

## Business Problem
Customer churn is a major revenue risk for SaaS companies, especially when disengagement
happens gradually and goes unnoticed. Losing an existing customer is significantly more
expensive than retaining one.

## Objective
The objective of this project is to proactively identify customers at risk of churn by
detecting early behavioral decline and enabling timely retention actions before cancellation.

## Approach
1. Generated daily SaaS event-level data to simulate real user behavior
2. Built customer behavior timelines from raw events
3. Detected early behavioral drift signals
4. Segmented customers into risk stages
5. Trained a churn prediction model using drift features
6. Recommended proactive retention actions


## Evaluation Strategy
Customer churn is an imbalanced problem where most customers do not churn.
In such cases, accuracy can be misleading, as a model predicting "no churn"
for all customers would still achieve high accuracy.

The final Random Forest model achieved a ROC–AUC of approximately 0.71,
demonstrating effective separation between churned and retained customers
in an early-warning churn detection setting.


## Key Features
- Event-level SaaS data modeling
- Behavioral drift detection (early warning)
- Risk-based customer segmentation
- Actionable churn prevention system

## Tech Stack
Python, Pandas, Scikit-learn

## Business Impact
Helps SaaS product teams identify disengaging users early and take proactive steps to reduce churn.
Key Business Insights

1. Customers showing a consistent decline in login frequency and feature usage
   are significantly more likely to churn, highlighting disengagement as an
   early and actionable churn signal.

2. Payment failures strongly correlate with high churn risk, indicating that
   billing friction and failed transactions are major contributors to customer loss.

3. Medium-risk customers represent the largest opportunity for retention, as
   timely engagement and product nudges can prevent escalation to high-risk churn.

4. Behavioral drift features provide earlier churn detection compared to using
   static customer attributes alone, enabling proactive intervention rather than
   reactive churn response.

5. Combining behavioral signals with machine learning allows product teams to
   prioritize retention efforts efficiently instead of applying uniform actions
   across all users.
