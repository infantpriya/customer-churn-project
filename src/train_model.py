import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
import joblib

def train_model():

    X_train = pd.read_csv("data/X_train.csv")
    y_train = pd.read_csv("data/y_train.csv")

    # Flatten y_train
    y_train = y_train.values.ravel()

    model = XGBClassifier(
        max_depth=5,
        learning_rate=0.1,
        n_estimators=200,
        subsample=0.8,
        colsample_bytree=0.8
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "data/churn_model.pkl")

    print("✔ Model training completed!")
    print("✔ Saved model → data/churn_model.pkl")

if __name__ == "__main__":
    train_model()
