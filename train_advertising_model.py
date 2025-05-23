import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import os

# read data
df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/Advertising.csv")

# Features and label
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
estimator = RandomForestRegressor(n_estimators=200)
estimator.fit(X_train, y_train)

# Evaluate
y_pred = estimator.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R2: {r2}")

# Save model
os.makedirs("saved_models", exist_ok=True)
joblib.dump(estimator, "saved_models/03.randomforest_with_advertising.pkl")
