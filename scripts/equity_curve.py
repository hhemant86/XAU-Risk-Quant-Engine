"""
Performance Visualization Engine:
Generates high-fidelity equity curves from multi-asset execution data.
Includes moving average overlays to identify performance momentum and structural shifts.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Institutional Path Logic
base_path = os.path.dirname(os.path.abspath(__file__))

# 2. Loading Versioned Data (Using your new naming convention)
# We load both 'stable' and 'volatile' to show the complete risk-adjusted lifecycle
try:
    path_stable = os.path.join(base_path, '..', 'data', 'stable_regime_data.csv')
    path_volatile = os.path.join(base_path, '..', 'data', 'volatile_regime_data.csv')
    
    df_s = pd.read_csv(path_stable)
    df_v = pd.read_csv(path_volatile)
    
    # Combine the datasets while ensuring no ticket duplication
    df = pd.concat([df_s, df_v]).drop_duplicates(subset='ticket')
    
    # 3. Sort by time for chronologically accurate plotting
    df['closing_time_utc'] = pd.to_datetime(df['closing_time_utc'], format='mixed')
    df = df.sort_values(by='closing_time_utc')

    # 4. Calculate Cumulative Profit
    df['cumulative_profit'] = df['profit_usd'].cumsum()

    # 5. Professional Plotting (Institutional Gold Theme)
    plt.style.use('dark_background') # Makes the gold line pop for LinkedIn
    plt.figure(figsize=(14, 7))
    plt.plot(df['closing_time_utc'], df['cumulative_profit'], color='#FFD700', linewidth=2, label='Portfolio Equity')
    
    # Adding a 50-trade Moving Average to identify structural shifts
    df['ma_50'] = df['cumulative_profit'].rolling(window=50).mean()
    plt.plot(df['closing_time_utc'], df['ma_50'], color='white', linestyle='--', alpha=0.5, label='50-Trade Momentum')

    plt.title('Institutional Equity Curve: XAU Risk Quant Engine ($425M+ Narrative)', fontsize=16, color='gold')
    plt.xlabel('Execution Timeline', fontsize=12)
    plt.ylabel('Cumulative P/L (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.2)

    # Save to the results folder
    output_path = os.path.join(base_path, '..', 'results', 'equity_curve.png')
    plt.savefig(output_path, bbox_inches='tight')
    print(f"✅ Performance Map saved to: {output_path}")

except Exception as e:
    print(f"❌ Visualization Error: {e}")
    print("💡 Check: Are both 'stable_regime_data.csv' and 'volatile_regime_data.csv' present in your data folder?")