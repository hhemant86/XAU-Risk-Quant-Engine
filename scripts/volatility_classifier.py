"""
Volatility Regime Classifier:
Uses rolling-window standard deviation to categorize market conditions into 
CALM, MODERATE, or EXTREME regimes for dynamic capital protection.
"""
import sqlite3
import pandas as pd
import numpy as np
import os

# 1. Setup
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')
conn = sqlite3.connect(db_path)

# 2. Load and Sort Data
query = "SELECT symbol, trade_date, price FROM zerodha_trades ORDER BY trade_date ASC"
df = pd.read_sql(query, conn)
conn.close()

# 3. Calculate Rolling Volatility (Window of 20 trades)
df['rolling_vol'] = df.groupby('symbol')['price'].transform(lambda x: x.rolling(window=20).std())

# 4. Define Regimes based on Percentiles
# Low Volatility: Bottom 25% | High Volatility: Top 25%
low_threshold = df['rolling_vol'].quantile(0.25)
high_threshold = df['rolling_vol'].quantile(0.75)

def classify_regime(vol):
    if pd.isna(vol): return "Insufficient Data"
    if vol <= low_threshold: return "CALM"
    if vol >= high_threshold: return "EXTREME"
    return "MODERATE"

df['regime'] = df['rolling_vol'].apply(classify_regime)

# 5. Output Intelligence
print("--- VOLATILITY REGIME REPORT ---")
print(df['regime'].value_counts())

# Save a sample to check the logic
df.tail(10).to_csv(os.path.join(base_path, '..', 'results', 'regime_sample.csv'))
print(f"\n✅ Regime classification complete. Sample saved to results/.")