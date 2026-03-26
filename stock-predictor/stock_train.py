import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import os

# ── Load data ──
print("Loading stock data...")
df = pd.read_csv('data/stock.csv')

# ── Use these columns: Open, High, Low, Volume to predict Close ──
features = ['Open', 'High', 'Low', 'Volume']
target   = 'Close'

# Drop rows with missing values
df = df[features + [target]].dropna()

X = df[features]
y = df[target]

print(f"Total rows loaded: {len(df)}")

# ── Split data ──
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ── Train model ──
print("Training Linear Regression model...")
model = LinearRegression()
model.fit(X_train, y_train)

# ── Evaluate ──
preds = model.predict(X_test)
mae   = mean_absolute_error(y_test, preds)
r2    = r2_score(y_test, preds)

print(f"\nResults:")
print(f"  Mean Absolute Error : {mae:.2f}")
print(f"  R2 Score            : {r2:.4f}")

# ── Save model ──
os.makedirs('model', exist_ok=True)
with open('model/stock_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\nDone! Model saved as model/stock_model.pkl")