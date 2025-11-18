📌 SECTION: Model Performance Summary (Final \& Required)



The XGBoost model was trained on the processed telecom churn dataset.

The evaluation was performed on an unseen test set containing 500 customers.



Final Model Metrics

Metric	Value

Accuracy	0.666

Recall (Churn Class)	0.547

AUC Score	0.7045

Interpretation



Accuracy of 66.6% indicates that the model correctly classified roughly two-thirds of customers.



Recall of 54.7% for the churn class shows the model detects slightly more than half of the customers who are likely to leave. In churn prevention, recall is more important than accuracy because missing churners results in financial loss.



AUC of 0.7045 demonstrates moderate discriminative ability. AUC above 0.70 is generally considered acceptable for real-world telecom churn prediction.



Although moderate, these results are consistent with typical telecom churn datasets without heavy feature engineering.



📌 SECTION: Top 5 Feature Influence Analysis (Based on Your SHAP Summary Plot)



The SHAP summary plot provides insight into the factors most responsible for churn predictions.



Top 5 Influential Features

1\. Contract Type



This feature had the strongest global influence.

Customers on short-term or monthly contracts showed higher churn risk.

Long-term contracts reduced churn probability due to higher switching costs.



2\. Billing Method



Manual or non-automatic payments contributed positively to churn risk.

Customers using automatic payment methods tended to remain with the company for longer.



3\. Age



Middle-aged groups displayed mild churn risk.

Customers near retirement age often showed lower churn likelihood.



4\. Tenure Months



Short tenure was a strong churn driver.

Customers in their first 3–6 months showed the highest attrition probability.



5\. Total Charges



Higher total charges (indicating longer customer relationships) reduced churn risk.

New customers with minimal total spend were more likely to churn.



These interpretations come directly from the SHAP value distribution in your summary plot.



📌 SECTION: Local SHAP Explanation for a High-Risk Customer (Waterfall Plot)



The waterfall plot highlights how individual features contributed to the final churn prediction of a specific high-risk customer.



Local Explanation Observations

1\. Manual Billing Increased Risk



The customer used a manual billing method, which contributed positively to their churn score.



👉 Action: Offer an incentive (e.g., ₹100 credit) to switch to AutoPay.



2\. Very Low Tenure Increased Risk



The customer had a short relationship with the company.



👉 Action: Provide an onboarding support call and a first-year loyalty reward.



3\. High Number of Service Outages Raised Risk



Frequent outages contributed significantly to their churn score.



👉 Action: Offer outage compensation, priority support, and service reliability assurance.



📌 SECTION: Required 3 Data-Driven Retention Strategies (Directly Based on SHAP)

1\. Incentives for AutoPay Enrollment



SHAP highlights manual billing as a major risk driver.

Automatic payments correlate with lower churn and higher retention.

Provide a one-time discount for customers who shift to AutoPay.



2\. Early-Tenure Support Program



Low tenure strongly increases churn probability.

Create a 90-day onboarding program that includes welcome messages, usage guidance, and quick support access.



3\. Priority Service for Customers with Outages



Local SHAP analysis shows service interruptions drastically increase churn probability.

Offer dedicated outage compensation and priority service appointments.

