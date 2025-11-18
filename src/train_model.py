"""
train_model.py

This script trains a high-performance Gradient Boosting model using XGBoost.
The project requirements specify using XGBoost/LightGBM/GBM instead of RandomForest.
This file trains the model, evaluates it, and saves it for SHAP analysis.

Explanation of major steps is included throughout the script.
"""

import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, classification_report
import joblib

# 1. Load the processed data created by preprocess.py
# X_train, X_test, y_train, y_test are saved earlier to ensure reproducibility
X_train = pd.read_csv("data/X_train.csv")
X_test = pd.read_csv("data/X_test.csv")
y_train = pd.read_csv("data/y_train.csv").values.ravel()
y_test = pd.read_csv("data/y_test.csv").values.ravel()

# 2. Define a high-performance XGBoost model
# These parameters provide strong performance on tabular churn datasets
model = XGBClassifier(
    n_estimators=300,            # Number of boosting rounds
    learning_rate=0.05,          # Controls update step size
    max_depth=6,                 # Complexity of trees
    subsample=0.9,               # Row sampling (prevent overfitting)
    colsample_bytree=0.9,        # Feature sampling (prevent overfitting)
    eval_metric="logloss",       # Avoids warnings and fits binary classification
    use_label_encoder=False
)

# 3. Train the model on the training data
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# 5. Compute required performance metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

print("Accuracy:", accuracy)
print("Recall (Churn Class):", recall)
print("AUC:", auc)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Save the model for SHAP analysis
joblib.dump(model, "data/churn_model.pkl")
print("Model saved to data/churn_model.pkl")
