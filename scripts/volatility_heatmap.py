"""
Behavioral Heatmapping:
Visualizes turnover density across a time-day matrix to identify peak liquidity exposure.
Provides a behavioral fingerprint of institutional-scale execution.
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Setup paths
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')
results_dir = os.path.join(base_path, '..', 'results')

# 2. Connect and Load Data
conn = sqlite3.connect(db_path)
query = "SELECT order_execution_time, quantity, price FROM zerodha_trades"
df = pd.read_sql(query, conn)
conn.close()

# 3. Data Engineering: Time Analysis
df['timestamp'] = pd.to_datetime(df['order_execution_time'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()
df['turnover'] = df['quantity'] * df['price']

# 4. Create the Heatmap Matrix
# We aggregate turnover by Day and Hour
heatmap_data = df.pivot_table(
    index='day_of_week', 
    columns='hour', 
    values='turnover', 
    aggfunc='sum'
).fillna(0)

# Sort days correctly
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
heatmap_data = heatmap_data.reindex(days_order)

# 5. Visualization: The Institutional Heatmap
plt.figure(figsize=(15, 8))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=False, cbar_kws={'label': 'Turnover (INR)'})

plt.title('Institutional Exposure Heatmap: Turnover by Time/Day', fontsize=16, pad=20)
plt.xlabel('Hour of Day (24h Format)', fontsize=12)
plt.ylabel('Day of Week', fontsize=12)

# Save the result for GitHub
output_path = os.path.join(results_dir, 'volatility_heatmap.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"✅ Heatmap generated successfully: {output_path}")