# XAU-Risk-Quant-Engine
Python-based quantitative risk engine analyzing $425M+ in XAU/XAG executions to detect drawdowns and volatility regimes.

📌 Project Overview
This project focuses on the systematic auditing and risk-profiling of high-notional trading data. By analyzing over $425 Million USD in cumulative turnover across global (Exness) and domestic (Zerodha) markets, this engine identifies institutional-scale drawdown triggers and volatility anomalies.

The objective is to move beyond manual execution by building a Volatility-Regime Classifier that automates capital protection during "Black Swan" events.

📊 Key Performance Metrics
Total Notional Turnover: ~$425,681,199.48 USD

Global Execution (Exness): $225M+ (Live) | $65M+ (Stress-Test Simulation)

Domestic Execution (Zerodha): ₹18.4 Crore+ (MCX & NSE)

Total Data Points: 7,451+ Verified Executions

Processing Efficiency: Vectorized audit completed in 0.0742 seconds on ASUS TUF A16.

🛡️ Risk Autopsy Findings
A critical component of this project is the Maximum Drawdown (MDD) analysis. The engine successfully identified a catastrophic "Black Tuesday" liquidity event in the simulation data.

Identified Max Drawdown: $-228,608.72

Critical Date: October 28, 2025

Primary Failure Mode: "Stop Out" (SO) clustering during high-volatility regimes.

🛠️ Technical Stack
Hardware: ASUS TUF A16 (Ryzen 7 7735HS, Radeon RX 7600S)

Mobile Command: Samsung S23 Ultra (Termux & Pydroid 3)

Languages: Python 3.12

Libraries: Pandas, NumPy, Matplotlib

Methodology: Vectorized data processing, Peak-to-Valley MDD algorithms.

📂 Project Structure
Plaintext

XAU-Risk-Quant-Engine/
├── data/               # Private tradebooks (Git-ignored)
├── scripts/
│   ├── audit.py             # Global execution turnover script
│   ├── equity_curve.py      # Visual timeline of P/L
│   └── drawdown_analysis.py # MDD and Risk Threshold logic
├── results/
│   ├── equity_curve.png     # Visualized performance
│   └── drawdown_analysis.png# Visualized risk profile
└── README.md           # Professional project documentation
🚀 Future Roadmap
Phase 1 (Current): Data Auditing & Risk Fingerprinting.

Phase 2: Machine Learning-based Volatility Forecasting (VIX Correlation).

Phase 3: Automated Webhook Integration for Real-time Capital Locking.

🤝 Contact
[Hemant Verma] Quantitative Research & AI Development [www.linkedin.com/in/hemant-verma-311b6031a] | [hemant.verma866@hotmail.com]

