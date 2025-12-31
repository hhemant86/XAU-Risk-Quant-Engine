
"""
Anomaly Detection Module
------------------------
Purpose:
Identify statistical outliers and tail-risk events in high-stakes financial datasets
as a preprocessing step for ML-based risk and volatility modeling.

Methods:
- 3-Sigma statistical filtering
- Distribution validation
- Noise vs tail-risk separation
"""

import os
import pandas as pd
import numpy as np

# 1. Professional Path Logic
# This automatically finds the 'data' folder one level up from 'scripts'
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data', 'stable_regime_data.csv')
results_dir = os.path.join(base_path, '..', 'results')

# Ensure the results directory exists so the script doesn't crash
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# 2. Load the $425M Notional Data Stream
try:
    df = pd.read_csv(data_path) # Loading Exness Live/Stable data
    
    # 3. Calculate Mean and Standard Deviation of Profit/Loss
    mean_pl = df['profit_usd'].mean()
    std_pl = df['profit_usd'].std()

    # 4. Outlier Logic: The 3-Standard Deviation (99.7%) Rule
    upper_limit = mean_pl + (3 * std_pl)
    lower_limit = mean_pl - (3 * std_pl)

    outliers = df[(df['profit_usd'] > upper_limit) | (df['profit_usd'] < lower_limit)]

    # 5. Institutional-Grade Reporting
    print(f"--- ANOMALY REPORT ---")
    print(f"Total Trades Analyzed: {len(df)}")
    print(f"Outliers Detected: {len(outliers)}")
    print(f"Normal Range: ${lower_limit:.2f} to ${upper_limit:.2f}")

    # 6. Export for Forensic Review
    output_path = os.path.join(results_dir, 'anomalies_found.csv')
    outliers.to_csv(output_path, index=False)
    print(f"\n✅ Success: {len(outliers)} anomalies saved to {output_path}")

except FileNotFoundError:
    print(f"❌ Error: Data file not found at {data_path}")
    print("Ensure your CSV is named 'stable_regime_data.csv' inside the 'data' folder.")