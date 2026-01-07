import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'results', 'live_market_data.csv')

def animate(i):
    if not os.path.exists(LOG_PATH): return
    try:
        data = pd.read_csv(LOG_PATH, on_bad_lines='skip').tail(35)
        plt.clf()
        
        # TOP: Liquidity & Reasoning
        plt.subplot(2, 1, 1)
        plt.plot(data['Timestamp'], data['BTC_Price'], color='#f2a900', marker='o', markersize=3)
        regime = data['Regime_Status'].iloc[-1]
        reason = data['Reasoning'].iloc[-1]
        plt.title(f"STATE: {regime} | {reason}", fontweight='bold', color='red' if "STRESS" in regime else "blue")
        plt.xticks([])

        # BOTTOM: Decision Zones
        plt.subplot(2, 1, 2)
        plt.plot(data['Timestamp'], data['Global_Ratio'], label='COMEX Ratio', color='cyan', linewidth=2)
        
        # Draw Governance Thresholds
        plt.axhline(y=62, color='red', linestyle='--', alpha=0.3, label='Squeeze Zone')
        plt.axhline(y=56, color='green', linestyle='--', alpha=0.3, label='Buy Zone')
        
        status = data['Margin_Status'].iloc[-1]
        plt.figtext(0.15, 0.02, f"GOVERNANCE: {status}", fontweight='bold', color='orange', bbox=dict(facecolor='black', alpha=0.1))
        
        plt.xticks(rotation=35, ha='right', fontsize=7)
        plt.legend(loc='upper left', fontsize=8)
        plt.tight_layout()
    except: pass

fig = plt.figure(figsize=(12, 8))
ani = FuncAnimation(fig, animate, interval=5000, cache_frame_data=False)
plt.show()