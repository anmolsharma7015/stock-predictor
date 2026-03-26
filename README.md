# Stock Price Predictor

A machine learning project that predicts the **Closing Price** of a stock using Open, High, Low prices and Volume — built with Linear Regression (scikit-learn).

---

## Folder Structure

```
stock-predictor/
├── data/
│   └── stock.csv          <- stock data goes here
├── model/
│   └── stock_model.pkl    <- auto-created after running train.py
├── train.py               <- run FIRST
├── predict.py             <- run to predict closing price
├── generate_data.py       <- run this if you have no stock data
└── README.md
```

---

## Install Libraries

Open VS Code terminal (`Ctrl+``) and run:

```
pip install scikit-learn pandas numpy
```

---

## How to Use

### Option A — Use Your Own Stock Data (Real Data)

**Step 1** — Download stock data from Yahoo Finance:
- Go to finance.yahoo.com
- Search any stock (e.g. RELIANCE, TCS, AAPL)
- Click Historical Data -> Download
- Save the CSV file as `stock.csv` inside the `data/` folder

Your CSV must have these columns:
```
Open, High, Low, Close, Volume
```

**Step 2** — Train the model:
```
python train.py
```

**Step 3** — Predict a closing price:
```
python predict.py
```

---

### Option B — Use Generated Sample Data (No Download Needed)

**Step 1** — Generate sample data:
```
python generate_data.py
```

**Step 2** — Train:
```
python train.py
```

**Step 3** — Predict:
```
python predict.py
```

---

## Example Output

### train.py
```
Loading stock data...
Total rows loaded: 500

Results:
  Mean Absolute Error : 8.43
  R2 Score            : 0.9921

Done! Model saved as model/stock_model.pkl
```

### predict.py
```
Stock Price Predictor ready!

Open Price  : 1520
High Price  : 1545
Low Price   : 1510
Volume      : 1200000

Predicted Close Price: 1531.24
```

---

## What the Model Learns

| Input Feature | What it means |
|---|---|
| Open Price | Price when market opened |
| High Price | Highest price of the day |
| Low Price  | Lowest price of the day |
| Volume     | Number of shares traded |
| **Close Price** | **What we predict** |

---

## How It Works

Uses **Linear Regression** — a simple, fast algorithm that finds the best straight line relationship between input features and the output (Close Price). It learns that Close Price is closely related to Open, High, and Low prices.

This is the same Transfer Learning concept — we use a pre-built algorithm (Linear Regression from scikit-learn) instead of building math from scratch.

---

## Files on GitHub

Upload only:
```
train.py
predict.py
generate_data.py
README.md
```

Do NOT upload `data/` or `model/`.

---

*Module 5 Project — Machine Learning | First Year AI/ML*
