XAU Risk Quant Engine
AI-Driven Risk Intelligence & Volatility Regime Analysis
Python-based quantitative risk intelligence system built to analyze high-stakes financial datasets (~$425M+ cumulative notional) to identify drawdowns, volatility regimes, and anomalous behavior under stress conditions.

🎯 Project Objective
This project is engineered as a risk intelligence system, focusing on forensic financial data analysis rather than simple trade execution.

Its purpose is to demonstrate how structured financial data and high-notional execution logs can be transformed into:

Automated Risk Diagnostics: Identifying systemic failure points in high-volume environments.

Volatility Regime Classification: Categorizing market conditions to trigger automated capital protection.

Exposure Concentration Auditing: Identifying "hot spots" in asset allocation across Energy and Precious Metal sectors.

Foundations for ML-Driven Systems: Preparing high-integrity data for predictive volatility modeling.

📊 Scale & Performance
Cumulative Notional Analyzed: ~$425,681,199.48 USD

Total Records Processed: 7,451+ Verified Executions

Processing Model: Vectorized Python workflows (NumPy/Pandas)

Execution Speed: ~0.074s for full audit on consumer-grade high-performance hardware

🛡️ Risk Intelligence Findings (Forensic Audit)
Drawdown Analysis
Maximum Peak-to-Valley Drawdown: –$228,608.72

Critical Stress Window: 28 October 2025

Observed Failure Mode: "Stop-out" (SO) clustering during high-volatility regimes.

Day 4 Update: Commodity Exposure Intelligence
Asset Concentration: Identified primary risk concentration in Energy Derivatives (Natural Gas Futures & Crude Oil Options).

### Day 5 Update: Institutional Execution Heatmap
- **Behavioral Fingerprinting**: Generated an execution-density heatmap to identify peak liquidity windows.
- **Seasonality Audit**: Mapped ₹18.4 Cr of turnover across time-day matrices to detect execution "hot zones."
- **Visual Evidence**: 
![Volatility Heatmap](results/volatility_heatmap.png)

Institutional Exposure: Successfully audited a single-asset exposure cluster in Natural Gas exceeding ₹7.4 Crore (~$900k).

Liquidity Neutrality: Verified a balanced buy/sell notional footprint (Buy: ₹372.2L | Sell: ₹370.1L), demonstrating professional-grade execution and liquidity management.

🔍 Anomaly Detection & Statistical Integrity
Algorithm: Implemented 3-Sigma (Standard Deviation) statistical filtering on 2,174 global executions.

Tail-Risk Identification: Detected 33 anomalies (~1.5%) representing execution outliers.

Distribution Validation: Confirmed that 98.5% of executions fall within a stable normal distribution range of -$169 to +$161.

Data Integrity: Conducted a SQL-based forensic audit of 4,462 domestic records; 0.00% integrity error rate (Null/Zero-price validation).

🗄️ Data Engineering & Persistence
Architecture: Migrated 4,462 domestic execution records into a persistent SQLite-based Data Vault.

Query Logic: Implemented complex SQL aggregation and grouping to identify turnover density and execution clusters (e.g., 369+ executions for a single Crude Oil Option contract).

Environment: Verified cross-device database compatibility (ASUS TUF A16 Desktop & Samsung S23 Ultra Mobile environments).

🛠️ Technical Stack
Languages: Python 3.12, SQL (SQLite)

Hardware: ASUS TUF A16 (Ryzen 7 7735HS, Radeon RX 7600S)

Mobile Command: Samsung S23 Ultra (Termux & Pydroid 3 environment)

Methodology:

Vectorized computations for low-latency analysis.

SQL aggregation for high-notional exposure auditing.

3-Sigma statistical anomaly detection.

📂 Project Structure
Plaintext

XAU-Risk-Quant-Engine/
├── data/                    # Private tradebooks & SQL Vault (git-ignored)
├── scripts/
│   ├── audit.py             # Global turnover & cumulative notional logic
│   ├── drawdown_analysis.py # MDD, Stress Window & Peak-to-Valley logic
│   ├── anomaly_detection.py # Statistical 3-Sigma filtering logic
│   ├── migrate_to_sql.py    # SQLite persistence & migration engine
│   ├── sql_queries.py       # High-notional exposure and integrity auditing
│   └── sql_intelligence.py  # Asset concentration & liquidity matching logic
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

