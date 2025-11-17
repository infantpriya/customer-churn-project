import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# Load data and model
X_train = pd.read_csv("data/X_train.csv")
model = joblib.load("data/churn_model.pkl")

# Create SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_train)

# ==============================================
# SAVE SHAP SUMMARY PLOT
# ==============================================
plt.figure(figsize=(12,8))
shap.summary_plot(shap_values.values, X_train, show=False)
plt.savefig("data/shap_summary.png", bbox_inches='tight')
plt.close()
print("SHAP summary plot saved to data/shap_summary.png")

# ==============================================
# SAVE SHAP WATERFALL PLOT
# ==============================================
sample_index = 0
single_shap = shap_values.values[sample_index][:, 1]

explanation = shap.Explanation(
    values=single_shap,
    base_values=explainer.expected_value[1],
    data=X_train.iloc[sample_index],
    feature_names=X_train.columns
)

plt.figure(figsize=(12, 8))
plt.ioff()
shap.plots.waterfall(explanation, show=False)
plt.savefig("data/waterfall_plot.png", bbox_inches='tight')
plt.close()

print("Waterfall plot saved to data/waterfall_plot.png")
