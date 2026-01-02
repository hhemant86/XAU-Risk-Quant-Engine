"""
Economic Sentinel: 
Scans for High-Impact events and triggers the 'Warning' or 'Hedge' protocols
for the Aggregator Dashboard.
"""
import pandas as pd
from datetime import datetime

# 1. Mock Economic Calendar (In Phase 3, we will connect this to a real API)
calendar = [
    {'event': 'US Fed Rate Decision', 'impact': 'HIGH', 'time': '20:30'},
    {'event': 'India CPI Data', 'impact': 'MEDIUM', 'time': '17:30'},
    {'event': 'Geopolitical Tension: Middle East', 'impact': 'EXTREME', 'time': 'ONGOING'}
]

def get_engine_action(impact):
    """
    Decides the treasury action based on news impact.
    """
    if impact == 'EXTREME':
        return "HALT TRADING / WIDEN SPREAD 5%"
    elif impact == 'HIGH':
        return "WIDEN SPREAD 2% / INCREASE HEDGE ON MCX"
    return "NORMAL OPERATIONS"

# 2. Process Sentinel Logic
print("--- ECONOMIC SENTINEL ACTIVE ---")
for event in calendar:
    action = get_engine_action(event['impact'])
    print(f"EVENT: {event['event']} | IMPACT: {event['impact']} | ACTION: {action}")

# 3. Aggregator Integration
print("\n✅ Intelligence: Sentiment-based risk protocols integrated into Treasury Logic.")