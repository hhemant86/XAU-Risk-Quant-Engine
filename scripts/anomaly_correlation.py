import sqlite3
import pandas as pd
import os

# 1. Setup
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')
conn = sqlite3.connect(db_path)

# 2. Load anomalies and all trades
# (Assuming your anomaly detection script saved a flag or we re-run logic)
query = "SELECT order_execution_time, quantity, price FROM zerodha_trades"
df = pd.read_sql(query, conn)
conn.close()

df['timestamp'] = pd.to_datetime(df['order_execution_time'])
df['hour'] = df['timestamp'].dt.hour
df['turnover'] = df['quantity'] * df['price']

# 3. Calculate 3-Sigma Threshold for Turnover
mean_turnover = df['turnover'].mean()
std_turnover = df['turnover'].std()
threshold = mean_turnover + (3 * std_turnover)

# 4. Filter "Tail Risk" Events
anomalies = df[df['turnover'] > threshold]

print(f"--- ANOMALY CORRELATION REPORT ---")
print(f"Total Anomalies Found: {len(anomalies)}")
print("\n📍 Hour Distribution of High-Risk Events:")
print(anomalies['hour'].value_counts().sort_index())