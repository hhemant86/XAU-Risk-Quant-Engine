import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Setup
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')
results_dir = os.path.join(base_path, '..', 'results')

# 2. Load Data (Focusing on your most active symbol for clarity)
conn = sqlite3.connect(db_path)
# Get Natural Gas or Crude (Adjust symbol if needed, or get top symbol)
query = """
SELECT symbol, trade_date, price, quantity 
FROM zerodha_trades 
WHERE symbol LIKE 'NATURALGAS%' 
ORDER BY trade_date ASC
"""
df = pd.read_sql(query, conn)
conn.close()

# 3. Calculate Volatility & Regime (Re-implementing logic for plotting)
df['vol'] = df['price'].rolling(window=20).std()
high_threshold = df['vol'].quantile(0.75)

# 4. Visualization: The "Stress Map"
plt.figure(figsize=(15, 7))
plt.plot(df.index, df['price'], color='gray', alpha=0.5, label='Asset Price')

# Overlay Extreme Points in RED
extreme_df = df[df['vol'] >= high_threshold]
plt.scatter(extreme_df.index, extreme_df['price'], color='red', label='EXTREME REGIME', s=10)

plt.title('Institutional Stress Map: Price Action vs. Volatility Regimes', fontsize=14)
plt.xlabel('Execution Sequence', fontsize=12)
plt.ylabel('Price (INR)', fontsize=12)
plt.legend()

# Save output
output_path = os.path.join(results_dir, 'regime_map.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"✅ Stress Map generated: {output_path}")