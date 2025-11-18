&nbsp;Customer Churn Prediction – SHAP Interpretability Project





Interpretability Analysis of Customer Churn Prediction Using SHAP



This project develops a churn prediction model using Gradient Boosting (XGBoost) and applies SHAP values to interpret both global and local model behavior. The analysis includes performance evaluation, feature importance interpretation, individual customer explanations, and retention strategies derived directly from SHAP outputs.



1\. Model Development and Performance Metrics



An XGBoost classifier was trained on the customer churn dataset. The dataset was divided into training and testing sets. The objective was to identify customers who are at risk of leaving and understand the factors that contribute to the model decision.



Model Performance Results



Accuracy: 0.666



Recall (Churn Class): 0.547



AUC: 0.705



Interpretation



The model correctly detects more than half of the customers who are likely to churn.



The AUC score of approximately 0.70 indicates moderate discriminative power.



Recall is important because retaining the at-risk group is the primary objective in churn prediction.



These metrics show that the model works sufficiently for interpretability and SHAP analysis.



2\. Global Feature Importance Using SHAP Summary Plot



SHAP values were computed for all features to understand how each one influences predictions across the entire dataset. The plot used is shap\_summary.png, saved in the data directory.



Top Five Most Influential Features



Contract Type



Month-to-month customers show the highest churn risk.



Long-term contracts reduce churn likelihood.



Billing Method



Manual or paper-based billing is linked with higher churn.



Automatic payments are associated with more stable customers.



Age



Younger customers demonstrate slightly higher churn tendencies.



Older customers tend to remain subscribed longer.



Total Charges



Customers with lower lifetime spending show higher churn probability.



This often reflects limited tenure or early dissatisfaction.



Tenure Months



Shorter tenure strongly correlates with churn.



Longer tenure customers exhibit more stability.



These insights are derived directly from the SHAP summary plot.



3\. Local SHAP Analysis Using a Waterfall Plot



A single test customer was selected to analyze the model decision. The explanation is stored in waterfall\_plot.png.



Key Local Insights



Contract Type reduced the predicted probability of churn.



Billing Method and Age also contributed to lowering churn risk.



Service Usage and Support Call Frequency added slight upward pressure toward churn.



This plot helps visualize how individual features push the prediction upward or downward for one customer.



4\. Retention Strategies Based on SHAP Explanations



All recommendations originate directly from the SHAP results and reflect the strongest predictive drivers.



Strategy 1: Improve the experience for month-to-month customers



Since contract type is the strongest churn indicator, providing incentives for switching to longer contracts may reduce churn.



Strategy 2: Encourage automatic billing adoption



Manual billing is associated with higher churn risk. Encouraging customers to switch to automatic payments through discounts or credits may reduce attrition.



Strategy 3: Strengthen early customer engagement



Customers with short tenure (< six months) have the highest churn probability.

Early onboarding programs and follow-up interactions can improve retention.



5\. Comparison Between Traditional Feature Importance and SHAP



Traditional feature importance reflects feature split gain but lacks directionality.



SHAP explains not only which features matter but also how they influence predictions.



SHAP identifies both global patterns and individual-level behavior.



In this project, both methods identify similar top features, but SHAP provides clearer interpretability needed for actionable decisions.



Deliverables Included



All required files are included in the repository:



data/shap\_summary.png



data/waterfall\_plot.png



src/train\_model.py



src/preprocess.py



src/explain\_model.py



notebooks/churn\_analysis.ipynb



notebooks/SHAP\_analysis\_of\_customer\_churn\_prediction.ipynb



These files reproduce the results described above.



Conclusion



This project completes the full interpretability workflow using XGBoost and SHAP. The analysis provides global and local insights into customer behavior, along with concrete retention strategies supported by SHAP explanations. This approach helps organizations understand not only who is likely to churn but also why those predictions occur.

