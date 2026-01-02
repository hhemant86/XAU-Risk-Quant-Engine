"""
Scenario Master:
Combines Audit Data with Institutional Sizing and Scenario Labeling.
Produces an 'Executive Risk Report' for the $425M portfolio.
"""
import pandas as pd
import os

# 1. Setup
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data', 'volatile_regime_data.csv')

def get_scenario_label(profit):
    """Assigns institutional labels based on the severity of the historical move."""
    if profit < -50000: return "BLACK SWAN: Geopolitical/Liquidity Gap"
    if profit < -20000: return "HIGH VOLATILITY: Central Bank Policy Shift"
    if profit < -5000:  return "MODERATE: Standard Market Correction"
    return "STABLE: Normal Trading Conditions"

try:
    # 2. Load and Process
    df = pd.read_csv(data_path)
    
    # Apply Scenario Labels
    df['scenario'] = df['profit_usd'].apply(get_scenario_label)

    # 3. Apply Institutional Sizing (Scaling down to 10% for high risk)
    def apply_mitigation(row):
        if "BLACK SWAN" in row['scenario']: return 0.05 # 95% reduction
        if "HIGH VOLATILITY" in row['scenario']: return 0.20 # 80% reduction
        return 1.0 # Full size for stable

    df['mitigated_profit'] = df['profit_usd'] * df['scenario'].apply(lambda x: 0.05 if "BLACK SWAN" in x else (0.20 if "HIGH" in x else 1.0))

    # 4. Generate Executive Report
    print("--- EXECUTIVE RISK SCENARIO REPORT ---")
    report = df.groupby('scenario').agg({
        'profit_usd': ['count', 'min', 'sum'],
        'mitigated_profit': 'sum'
    })
    print(report)

    # 5. Export for Portfolio Proof
    results_path = os.path.join(base_path, '..', 'results', 'executive_risk_report.csv')
    df.to_csv(results_path, index=False)
    print(f"\n✅ Professional Portfolio Proof saved to: {results_path}")

except Exception as e:
    print(f"❌ Scenario Master Error: {e}")