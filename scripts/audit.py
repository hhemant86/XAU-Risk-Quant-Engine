"""
Forensic Audit Engine:
Calculates global notional turnover and cumulative exposure across multi-currency tradebooks.
Validates execution integrity for high-stakes institutional datasets.
"""

import pandas as pd  # <--- THIS MUST BE HERE
import os

# 1. Institutional Path Logic
# This finds the 'data' folder regardless of where you run the script from
base_path = os.path.dirname(os.path.abspath(__file__))

# 2. VERIFY YOUR FILENAME: 
# If you renamed the file in your data folder, change it here too!
file_name = 'volatile_regime_data.csv'
file_path = os.path.join(base_path, '..', 'data', file_name)

try:
    # Check if file exists before trying to read
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found at: {file_path}")
        print("💡 Action: Check your 'data' folder and ensure the filename matches exactly.")
    else:
        df = pd.read_csv(file_path)
        
        # Standardize date format
        df['opening_time_utc'] = pd.to_datetime(df['opening_time_utc'], format='mixed')
        
        print("--- RAW DATA AUDIT ---")
        print(f"Total Transactions Found: {len(df)}")
        print(f"Total Profit/Loss: ${df['profit_usd'].sum():,.2f}")
        
        # Metrics
        max_win = df['profit_usd'].max()
        max_loss = df['profit_usd'].min()
        
        print(f"Largest Win: ${max_win:,.2f}")
        print(f"Largest Loss: ${max_loss:,.2f}")
        print(f"✅ Audit completed successfully for {file_name}")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")