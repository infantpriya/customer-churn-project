import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

def explain_model():

    model = joblib.load("data/churn_model.pkl")
    X_train = pd.read_csv("data/X_train.csv")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_train)

    print("✔ Generating SHAP summary plot...")
    shap.summary_plot(shap_values.values, X_train)
    plt.savefig("data/shap_summary.png")
    plt.close()

    print("✔ Generating SHAP bar plot...")
    shap.plots.bar(shap_values, show=False)
    plt.savefig("data/shap_bar.png")
    plt.close()

    print("✔ SHAP analysis completed!")
    print("✔ Plots saved in data/")

if __name__ == "__main__":
    explain_model()
