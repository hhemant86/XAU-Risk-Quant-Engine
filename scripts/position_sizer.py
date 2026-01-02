"""
Dynamic Position Sizing Engine:
Calculates risk-adjusted lot sizes based on Phase 1 Volatility Regimes.
Ensures capital preservation during 'Extreme' market conditions.
"""
import pandas as pd
import os

# 1. Path Configuration
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data', 'volatile_regime_data.csv')

# 2. Institutional Risk Parameters
ACCOUNT_EQUITY = 100000  # Base Equity for Simulation
MAX_RISK_PER_TRADE = 0.01  # 1% Rule
STOP_LOSS_PIPS = 50       # Average SL for XAU/USD

def calculate_dynamic_size(regime):
    """
    Returns a multiplier based on the identified market regime.
    """
    multipliers = {
        'CALM': 1.0,      # Full position size
        'MODERATE': 0.5,  # 50% reduction in risk
        'EXTREME': 0.1,   # 90% reduction (Survival Mode)
        'OUTLIER': 0.0    # Kill-Switch (No entry)
    }
    return multipliers.get(regime, 0.5)

try:
    # 3. Load Regime Data
    df = pd.read_csv(data_path)
    
    # Simulate a 'Regime' column if not already present from Phase 1
    # In a real run, this pulls from your volatility_classifier results
    if 'regime' not in df.columns:
        df['regime'] = 'MODERATE' # Defaulting for demonstration

    # 4. Apply Logic
    print("--- DYNAMIC POSITION SIZING REPORT ---")
    base_size = (ACCOUNT_EQUITY * MAX_RISK_PER_TRADE) / STOP_LOSS_PIPS
    
    df['adjusted_lot_size'] = df['regime'].apply(calculate_dynamic_size) * base_size
    
    # 5. Summary Output
    summary = df.groupby('regime')['adjusted_lot_size'].mean()
    print(summary)
    print("\n✅ Intelligence: Position Sizing table generated based on Volatility Regimes.")

except Exception as e:
    print(f"❌ Error: {e}")


# 5. Summary Output & Export
summary = df.groupby('regime')['adjusted_lot_size'].mean().reset_index()
    
    # Define the output path
results_path = os.path.join(base_path, '..', 'results', 'position_sizing_table.csv')
    
    # Save the file
summary.to_csv(results_path, index=False)
    
print("--- DYNAMIC POSITION SIZING REPORT ---")
print(summary)
print(f"\n✅ Intelligence saved to: {results_path}")        