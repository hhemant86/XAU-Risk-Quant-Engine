XAU Risk Quant Engine
AI-Driven Risk Intelligence & Volatility Regime Analysis
Python-based quantitative risk intelligence system built to analyze high-stakes financial datasets (~$425M+ cumulative notional) to identify drawdowns, volatility regimes, and anomalous behavior under stress conditions.

🎯 Project Objective
This project is engineered as a risk intelligence system, focusing on forensic financial data analysis rather than simple trade execution.

Its purpose is to demonstrate how structured financial data and high-notional execution logs can be transformed into:

Automated Risk Diagnostics: Identifying systemic failure points in high-volume environments.

Volatility Regime Classification: Categorizing market conditions to trigger automated capital protection.

Statistical Anomaly Detection: Filtering "noise" and "tail-risk" from institutional-grade datasets.

Foundations for ML-Driven Systems: Preparing high-integrity data for predictive volatility modeling.

The long-term roadmap evolves this engine into a machine learning–based risk classifier suitable for production-grade financial intelligence environments.

📊 Scale & Performance
Cumulative Notional Analyzed: ~$425,681,199.48 USD

Total Records Processed: 7,451+ Verified Executions

Processing Model: Vectorized Python workflows (NumPy/Pandas)

Execution Speed: ~0.074s for full audit on consumer-grade high-performance hardware

🛡️ Risk Intelligence Findings (Forensic Audit)
Drawdown Analysis
Maximum Peak-to-Valley Drawdown: –$228,608.72

Critical Stress Window: 28 October 2025

Observed Failure Mode: "Stop-out" (SO) clustering during high-volatility regimes

These findings reflect liquidity-driven cascading risk patterns typical of institutional-scale exposure in precious metal markets.

🔍 Anomaly Detection & Statistical Integrity
Algorithm: Implemented 3-Sigma (Standard Deviation) statistical filtering on 2,174 global executions.

Tail-Risk Identification: Detected 33 anomalies (~1.5%) representing execution outliers.

Distribution Validation: Confirmed that 98.5% of executions fall within a stable normal distribution range of -$169 to +$161.

Outcome: Ensures data robustness and removes "fat-finger" noise before entering Machine Learning training phases.

🗄️ Data Engineering & Persistence
Architecture: Migrated 4,462 domestic execution records into a persistent SQLite-based Data Vault.

Performance: Enabled high-concurrency historical querying for rapid risk audits and backtesting.

Environment Consistency: Verified cross-device database compatibility (ASUS TUF A16 Desktop & Samsung S23 Ultra Mobile environments).

🛠️ Technical Stack
Languages: Python 3.12, SQL (SQLite)

Hardware: ASUS TUF A16 (Ryzen 7 7735HS, Radeon RX 7600S)

Mobile Command: Samsung S23 Ultra (Termux & Pydroid 3 environment)

Methodology:

Vectorized computations for low-latency analysis.

Peak-to-valley drawdown detection algorithms.

3-Sigma statistical anomaly detection.

Relational data modeling for financial persistence.

📂 Project Structure
Plaintext

XAU-Risk-Quant-Engine/
├── data/                    # Private tradebooks & SQL Vault (git-ignored)
├── scripts/
│   ├── audit.py             # Global turnover & cumulative notional logic
│   ├── equity_curve.py      # P/L timeline reconstruction logic
│   ├── drawdown_analysis.py # MDD, Stress Window & Peak-to-Valley logic
│   ├── anomaly_detection.py # Statistical 3-Sigma filtering logic
│   ├── migrate_to_sql.py    # SQLite persistence & migration engine
│   └── zerodha_portfolio.py # Domestic portfolio segment analytics
├── results/
│   ├── equity_curve.png     # Visualized performance data
│   └── drawdown_analysis.png# Visualized risk & drawdown profile
├── README.md                # Institutional-grade project documentation
└── .gitignore               # Security & data privacy configurations
🚀 Future Roadmap
Phase 1 (Current): Data Engineering, Forensic Auditing & Statistical Fingerprinting.

Phase 2: Machine Learning-based Volatility Regime Forecasting & VIX Correlation.

Phase 3: Automated Webhook Integration for Real-time Capital Exposure Locking.

🤝 Contact & Professional Profile
Hemant Verma Quantitative Research & Risk Intelligence
[www.linkedin.com/in/hemant-verma-311b6031a] | [hemant.verma866@hotmail.com]

