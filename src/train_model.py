import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv").values.ravel()
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, "data/churn_model.pkl")
print('Model trained and saved to data/churn_model.pkl')
