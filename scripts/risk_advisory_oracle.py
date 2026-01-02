"""
Advisory Oracle: 
Uses simulated NLP/LLM logic to process news and generate 
SL/TP and Lot-Size advice for MCX/COMEX traders.
"""
import pandas as pd

def generate_advice(news_headline, capital_inr):
    # Simulated Sentiment Analysis (AI/ML Logic)
    # In Phase 3, we connect this to an actual LLM API
    risk_score = 0
    if "war" in news_headline.lower() or "crisis" in news_headline.lower():
        risk_score = 10
        advice = "⚠️ BLACK SWAN WARNING: HALT ALL TRADES. VOLATILITY EXCEEDS 3-SIGMA."
        lot_size = 0
    elif "fed" in news_headline.lower():
        risk_score = 5
        advice = "MODERATE VOLATILITY: REDUCE LOT SIZE. TARGET TP AT 1% MOVE."
        lot_size = round((capital_inr / 100000) * 0.5, 2)
    else:
        advice = "STABLE REGIME: PROCEED WITH CAUTION. FOLLOW STANDARD SL/TP."
        lot_size = round((capital_inr / 100000) * 1.0, 2)
        
    return advice, lot_size

# Simulation Run
news = "Geopolitical Tension: Crisis in Middle East impacts energy prices"
user_capital = 500000 # 5 Lakh INR

advice_text, recommended_lots = generate_advice(news, user_capital)

print("--- AI ADVISORY ORACLE OUTPUT ---")
print(f"HEADLINE: {news}")
print(f"CAPITAL:  ₹{user_capital:,.2f}")
print(f"ADVICE:   {advice_text}")
print(f"LOT SIZE: {recommended_lots} (Recommended for MCX)")