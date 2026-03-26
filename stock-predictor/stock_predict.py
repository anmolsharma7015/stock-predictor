import pickle
import numpy as np

# ── Load model ──
print("Loading model...")
with open('model/stock_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Stock Price Predictor ready!\n")
print("Enter stock values to predict the Closing Price.")
print("Type 'quit' to exit.\n")

while True:
    try:
        open_price = input("Open Price  : ")
        if open_price.lower() == 'quit':
            break

        high_price  = float(input("High Price  : "))
        low_price   = float(input("Low Price   : "))
        volume      = float(input("Volume      : "))
        open_price  = float(open_price)

        features = np.array([[open_price, high_price, low_price, volume]])
        predicted = model.predict(features)[0]

        print(f"\nPredicted Close Price: {predicted:.2f}\n")
        print("-" * 35)

    except ValueError:
        print("Please enter valid numbers.\n")
    except KeyboardInterrupt:
        break