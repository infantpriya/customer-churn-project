import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data():
    # Load dataset
    df = pd.read_csv("data/project_customer_churn_dataset.csv")

    # Drop customerID
    df = df.drop("customerID", axis=1)

    # Convert TotalCharges
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing values
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

    # Encode categorical variables
    df = pd.get_dummies(df, drop_first=True)

    # Split input & target
    X = df.drop("Churn_Yes", axis=1)
    y = df["Churn_Yes"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Save processed files
    X_train.to_csv("data/X_train.csv", index=False)
    X_test.to_csv("data/X_test.csv", index=False)
    y_train.to_csv("data/y_train.csv", index=False)
    y_test.to_csv("data/y_test.csv", index=False)

    print("✔ Data preprocessing completed and saved!")

if __name__ == "__main__":
    load_and_preprocess_data()
