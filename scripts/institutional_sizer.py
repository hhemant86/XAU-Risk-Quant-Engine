"""
Institutional Position Sizer:
Uses Continuous Scaling and Scenario-Aware Multipliers.
Replaces the old 'bucketed' position_sizer.py.
"""
import pandas as pd
import numpy as np

# Institutional Params
EQUITY = 100000
MAX_RISK = 0.02 # 2% Institutional Cap

def calculate_institutional_size(volatility_score):
    # Continuous Scaling Logic: Size shrinks as volatility grows
    # Base size * (1 - normalized_volatility)
    base_size = (EQUITY * MAX_RISK) / 50 
    multiplier = max(0, 1 - (volatility_score / 10)) # Scales down to 0 at score 10
    return base_size * multiplier

# Mock Data for Full Matrix Coverage
scenarios = {
    'CALM': 1.5,
    'MODERATE': 4.5,
    'EXTREME': 8.5,
    'OUTLIER': 11.0
}

print("--- INSTITUTIONAL RISK MATRIX ---")
for regime, score in scenarios.items():
    size = calculate_institutional_size(score)
    status = "HALT" if size == 0 else "ACTIVE"
    print(f"REGIME: {regime:<10} | VOL_SCORE: {score:<4} | SIZE: {size:<6.2f} | STATUS: {status}")

print("\n✅ Upgrade: Continuous scaling and full matrix coverage active.")

# ... existing logic ...
for regime, score in scenarios.items():
    size = calculate_institutional_size(score)
# ELITE REFINEMENT: EXTREME is now RESTRICTED
    if regime == 'EXTREME':
        status = "RESTRICTED (DELEVERAGED)"
        size = min(size, 2.0) # Cap at 2 units
    elif size == 0:
        status = "HALT"
    else:
        status = "ACTIVE"
    print(f"REGIME: {regime:<10} | VOL_SCORE: {score:<4} | SIZE: {size:<6.2f} | STATUS: {status}")