"""
Performance Visualization Engine:
Generates high-fidelity equity curves from multi-asset execution data.
Includes moving average overlays to identify performance momentum and structural shifts.
"""
import sqlite3
import pandas as pd
import os

# 1. Path Setup
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')

conn = sqlite3.connect(db_path)

print("--- DOMESTIC EXPOSURE INTELLIGENCE ---")

# QUERY: Identify "Exposure Clusters" 
# We calculate turnover (qty * price) and group it by Symbol and Trade Type (Buy/Sell)
query_exposure = """
SELECT 
    symbol, 
    trade_type, 
    SUM(quantity * price) as total_turnover,
    COUNT(*) as execution_count
FROM zerodha_trades 
GROUP BY symbol, trade_type 
ORDER BY total_turnover DESC 
LIMIT 10;
"""

exposure_report = pd.read_sql(query_exposure, conn)

# Format the turnover for easier reading (Senior Data Analyst Skill)
exposure_report['total_turnover_in_lakhs'] = exposure_report['total_turnover'] / 100000

print("\n📍 Top 10 Exposure Clusters (by Turnover):")
print(exposure_report[['symbol', 'trade_type', 'total_turnover_in_lakhs', 'execution_count']])

conn.close()