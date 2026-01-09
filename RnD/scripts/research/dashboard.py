import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression
import os
import time

# 1. INSTITUTIONAL PAGE CONFIG
st.set_page_config(
    page_title="SENTINEL PRIME | AI PREDICT",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. PATH ALIGNMENT
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "results", "integrated_audit.csv"))

def load_data():
    if os.path.exists(LOG_PATH):
        try:
            return pd.read_csv(LOG_PATH)
        except: return pd.DataFrame()
    return pd.DataFrame()

# 3. PREDICTIVE ENGINE (The Billionaire Edge)
def predict_next_move(df):
    if len(df) < 10: return None
    # Use last 10 ticks to forecast the next move using Linear Regression
    y = df['Z-Score'].tail(10).values
    X = np.arange(len(y)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[len(y)]])[0] # Predict the t+1 point
    return prediction

# 4. HEADER & GLOBAL STATUS
st.title("🛰️ SENTINEL PRIME : PREDICTIVE COMMAND")
st.caption(f"RnD Institutional Layer v2.2 | Data Stream: {LOG_PATH}")

df = load_data()

if not df.empty:
    last_row = df.iloc[-1]
    forecast = predict_next_move(df)
    
    # 5. DYNAMIC RISK ALERT SYSTEM
    # Visually flag if the system is currently locked or in stress
    gov_status = last_row['Governance']
    if "LOCK" in gov_status or "ALERT" in gov_status:
        st.error(f"🚨 CRITICAL: {gov_status}")
    elif last_row['State'] == "ANOMALY":
        st.warning("⚠️ WARNING: Market Anomaly Detected - High Divergence Risk")
    else:
        st.success("✅ SYSTEM NOMINAL: AI & Quant signals aligned.")

    # 6. KPI METRICS GRID
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric("Live Z-Score", f"{last_row['Z-Score']:.2f}")
    
    with m2:
        if forecast is not None:
            delta_val = forecast - last_row['Z-Score']
            st.metric("30s Forecast", f"{forecast:.2f}", delta=f"{delta_val:.2f} Prediction")
        else:
            st.metric("30s Forecast", "Learning...")

    with m3:
        st.metric("AI Sentiment", f"{last_row['Sentiment']:.4f}")

    with m4:
        st.metric("Market Regime", last_row['State'])

    # 7. VISUAL INTELLIGENCE
    
    c1, c2 = st.columns(2)
    
    with c1:
        # Volatility Line with Anomaly Threshold
        fig_z = px.line(df, x='Timestamp', y='Z-Score', title="Volatility Pipeline", template="plotly_dark")
        fig_z.add_hline(y=3.0, line_dash="dash", line_color="red", annotation_text="Anomaly")
        st.plotly_chart(fig_z, width="stretch")

    with c2:
        # AI Sentiment Signal Distribution
        fig_s = px.bar(df, x='Timestamp', y='Sentiment', title="FinBERT Sentiment Signal",
                       color='Sentiment', color_continuous_scale='RdYlGn', template="plotly_dark")
        st.plotly_chart(fig_s, width="stretch")

    # 8. INSTITUTIONAL AUDIT TRAIL
    st.subheader("🏛️ Forensic Audit Log")
    st.dataframe(df.sort_index(ascending=False), width="stretch")

else:
    st.info("Syncing with Quant Engine... Ensure 'ai_sentiment_sentinel.py' is running.")

# 9. AUTO-REFRESH (Standard 10s loop)
time.sleep(10)
st.rerun()