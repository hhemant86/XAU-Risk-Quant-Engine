"""
Drawdown & Stress Analysis Module
--------------------------------
Purpose:
Quantify peak-to-valley drawdowns and identify stress windows
that characterize regime shifts and systemic risk exposure.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Path Logic (Designed for your ASUS TUF A16 folder structure)
# This tells Python to go up from /scripts to /data
base_path = os.path.dirname(os.path.abspath(__file__))
live_path = os.path.join(base_path, '..', 'data', 'stable_regime_data.csv')
sim_path = os.path.join(base_path, '..', 'data', 'volatile_regime_data.csv')

# 2. Loading and Merging Data
try:
    df_live = pd.read_csv(live_path)
    df_sim = pd.read_csv(sim_path)
    print("✅ Files Loaded Successfully!")
    
    # Combine the Live and Simulation data to see the "Full Story"
    df = pd.concat([df_live, df_sim]).drop_duplicates(subset='ticket')
    print(f"✅ Data combined: {len(df)} total trades processed.")
    
    # 3. Data Cleaning
    df['closing_time_utc'] = pd.to_datetime(df['closing_time_utc'], format='mixed')
    df = df.sort_values(by='closing_time_utc')
    
    # 4. Maximum Drawdown (MDD) Calculation
    df['cumulative_profit'] = df['profit_usd'].cumsum()
    df['peak'] = df['cumulative_profit'].cummax()
    df['drawdown'] = df['cumulative_profit'] - df['peak']
    max_drawdown = df['drawdown'].min()
    
    # 5. Professional Reporting
    print(f"\n--- RISK AUTOPSY REPORT ---")
    print(f"Total Transactions: {len(df)}")
    print(f"Maximum Peak-to-Valley Loss: ${max_drawdown:,.2f}")
    
    # 6. Visualization (Using 'plt' defined above)
    plt.figure(figsize=(12, 6))
    plt.fill_between(df['closing_time_utc'], df['drawdown'], color='red', alpha=0.3)
    plt.plot(df['closing_time_utc'], df['drawdown'], color='red', linewidth=1)
    
    plt.title('Drawdown Profile: Identifying the Institutional Risk Threshold', fontsize=14)
    plt.xlabel('Timeline', fontsize=10)
    plt.ylabel('Drawdown (USD)', fontsize=10)
    plt.grid(True, alpha=0.2)
    
    # Ensure /results directory exists
    results_dir = os.path.join(base_path, '..', 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        
    plt.savefig(os.path.join(results_dir, 'drawdown_analysis.png'))
    print(f"\n✅ Drawdown chart successfully saved in: /results/drawdown_analysis.png")

except Exception as e:
    print(f"❌ An error occurred: {e}")
    print("Tip: Make sure your CSV files are inside the 'data' folder and named correctly.")