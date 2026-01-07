import requests
import pandas as pd
import yfinance as yf
import time
import os
import numpy as np
from datetime import datetime

# --- INSTITUTIONAL CACHE (Sticky Data) ---
# Prevents 0-value glitches during API downtime
LAST_VALID_DATA = {
    "BTC": 92600.0, 
    "XAU": 2650.0, 
    "XAG": 31.50, 
    "G_MCX": 75000.0, 
    "S_MCX": 92000.0
}

# --- PATH CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, '..', 'results', 'live_market_data.csv')
AUDIT_PATH = os.path.join(BASE_DIR, '..', 'results', 'regime_audit.csv')

# Ensure directory structure exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def get_live_data():
    """
    Ultimate Level 4 Fetcher:
    - Multi-stage fallback
    - Individual asset error isolation
    - Forward-fill caching (Sticky Data)
    """
    global LAST_VALID_DATA
    
    # 1. BTC PROXY (BINANCE)
    try:
        btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        btc_res = requests.get(btc_url, timeout=5).json()
        if 'price' in btc_res:
            LAST_VALID_DATA["BTC"] = float(btc_res['price'])
    except Exception as e:
        print(f"⚠️ BTC Feed Blip: Using {LAST_VALID_DATA['BTC']}")

    # 2. GLOBAL BULLION (COMEX)
    try:
        # We use 5d period to ensure we always have a 'last known price' even on slow days
        global_m = yf.download(tickers="GC=F SI=F", period="5d", interval="1m", progress=False)
        if not global_m.empty:
            # .ffill() handles any specific missing minutes
            latest_g = global_m['Close'].ffill().iloc[-1]
            if 'GC=F' in latest_g: LAST_VALID_DATA["XAU"] = float(latest_g['GC=F'])
            if 'SI=F' in latest_g: LAST_VALID_DATA["XAG"] = float(latest_g['SI=F'])
    except Exception:
        pass # Cache handles it

    # 3. INDIAN PROXIES (MCX)
    try:
        # 5m interval is much more stable for NSE ETF data on Yahoo Finance
        india_m = yf.download(tickers="GOLDBEES.NS SILVERBEES.NS", period="5d", interval="5m", progress=False)
        if not india_m.empty:
            latest_i = india_m['Close'].ffill().iloc[-1]
            if 'GOLDBEES.NS' in latest_i: 
                LAST_VALID_DATA["G_MCX"] = float(latest_i['GOLDBEES.NS']) * 1000
            if 'SILVERBEES.NS' in latest_i: 
                LAST_VALID_DATA["S_MCX"] = float(latest_i['SILVERBEES.NS']) * 100
    except Exception:
        pass # Cache handles it

    return LAST_VALID_DATA.copy()

def calculate_regime(df):
    """Institutional State Detection using Z-Score & Momentum Bias."""
    if len(df) < 20: 
        return "WARMING_UP", "Calibrating Baselines (N < 20)"
    
    prices = df['BTC_Price'].tail(20)
    mean_val = prices.mean()
    std_val = prices.std()
    
    # Statistical Anomaly Detection (Z-Score)
    z_score = abs((prices.iloc[-1] - mean_val) / std_val) if std_val > 0 else 0
    
    # Directional Bias (Short vs Long EMA Proxy)
    ema_short = prices.tail(5).mean()
    ema_long = prices.tail(15).mean()
    bias = "UP" if ema_short > ema_long else "DOWN"

    # Escalation Logic
    if z_score > 2.5: 
        return "ANOMALY_DETECTION", f"Z-Score {z_score:.2f} Extreme"
    if z_score > 1.5: 
        return "INSTITUTIONAL_STRESS", f"Z-Score {z_score:.2f} High"
    
    return f"STABILIZING_{bias}", f"Momentum {bias}"

def run_sentinel():
    """Main Execution Loop for Governance."""
    feeds = get_live_data()
    
    # Decision Ratios
    global_ratio = round(feeds["XAU"] / feeds["XAG"], 2) if feeds["XAG"] > 0 else 0
    mcx_ratio = round(feeds["G_MCX"] / feeds["S_MCX"], 2) if feeds["S_MCX"] > 0 else 0
    
    # Governance Status (Factory Decision Support)
    margin = "NEUTRAL_ACCUMULATION"
    if global_ratio > 62: 
        margin = "MARGIN_SQUEEZE_RISK"
    elif global_ratio < 56: 
        margin = "METAL_STRESS_BUY_ZONE"
    
    # State persistence
    if os.path.exists(LOG_PATH):
        try: history = pd.read_csv(LOG_PATH, on_bad_lines='skip')
        except: history = pd.DataFrame()
    else: history = pd.DataFrame()

    # Determine Regime & Reasoning
    regime, reason = calculate_regime(pd.concat([history, pd.DataFrame([{'BTC_Price': feeds['BTC']}])]))
    
    current_row = {
        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'BTC_Price': feeds["BTC"], 
        'XAU_USD': feeds["XAU"], 'XAG_USD': feeds["XAG"],
        'Global_Ratio': global_ratio, 'MCX_Ratio': mcx_ratio,
        'Margin_Status': margin, 'Regime_Status': regime, 'Reasoning': reason
    }
    
    # Record Audit Shifts
    if not history.empty and history['Regime_Status'].iloc[-1] != regime:
        audit_log = pd.DataFrame([{
            'Time': current_row['Timestamp'], 
            'Shift': f"{history['Regime_Status'].iloc[-1]} -> {regime}", 
            'Reason': reason
        }])
        audit_log.to_csv(AUDIT_PATH, mode='a', header=not os.path.exists(AUDIT_PATH), index=False)
        print(f"🚨 GOVERNANCE SHIFT: {regime} ({reason})")

    # Data Persistence with Write-Protection Retry
    for _ in range(5):
        try:
            pd.DataFrame([current_row]).to_csv(LOG_PATH, mode='a', header=not os.path.exists(LOG_PATH), index=False)
            print(f"✅ [{current_row['Timestamp'][-8:]}] BTC: ${feeds['BTC']:.0f} | Ratio: {global_ratio} | {regime}")
            break
        except PermissionError:
            time.sleep(0.5)

if __name__ == "__main__":
    print("="*60)
    print(f"{'🛰️ LEVEL 4 GOVERNANCE SENTINEL ACTIVE':^60}")
    print("="*60)
    while True:
        try:
            run_sentinel()
            time.sleep(30)
        except KeyboardInterrupt:
            print("\n🛑 System gracefully terminated by user.")
            break
        except Exception as e:
            print(f"⚠️ Runtime Alert: {e}")
            time.sleep(5)