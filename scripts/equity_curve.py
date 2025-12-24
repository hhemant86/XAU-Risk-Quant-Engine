import pandas as pd
import matplotlib.pyplot as plt

# 1. Load BOTH files to see the full $500M volume story
df1 = pd.read_csv('data/01_01_2007-23_12_2025 (1).csv')
df2 = pd.read_csv('data/01_01_2007-23_12_2025.csv')
df = pd.concat([df1, df2]).drop_duplicates(subset='ticket')

# 2. Sort by time to see the progression
df['closing_time_utc'] = pd.to_datetime(df['closing_time_utc'], format='mixed')
df = df.sort_values(by='closing_time_utc')

# 3. Calculate Cumulative Profit
df['cumulative_profit'] = df['profit_usd'].cumsum()

# 4. Plot the results
plt.figure(figsize=(12, 6))
plt.plot(df['closing_time_utc'], df['cumulative_profit'], color='gold', linewidth=2)
plt.title('XAU/USD Lifecycle: The $500M Equity Curve', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Cumulative P/L (USD)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('equity_curve.png')
print("✅ Chart saved as equity_curve.png. Open it now!")