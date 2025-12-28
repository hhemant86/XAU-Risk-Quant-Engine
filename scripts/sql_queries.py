import sqlite3
import pandas as pd
import os

# 1. Path Setup
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')

# 2. Connect to the Vault
conn = sqlite3.connect(db_path)

print("--- DAY 4: SQL INTELLIGENCE REPORT ---")

# QUERY A: The "Big Wins" (Identifying Profit Outliers)
# Finding trades where profit was > ₹10,000 to analyze successful regimes
query_wins = "SELECT symbol, quantity, price, (quantity * price) as turnover FROM zerodha_trades WHERE (quantity * price) > 50000 LIMIT 5"
big_trades = pd.read_sql(query_wins, conn)

print("\n📍 Top 5 High-Notional Executions (>₹50k):")
print(big_trades)

# QUERY B: Symbol Performance Aggregation
# This shows which asset you mastered best
query_symbols = "SELECT symbol, COUNT(*) as trade_count FROM zerodha_trades GROUP BY symbol ORDER BY trade_count DESC LIMIT 5"
symbol_stats = pd.read_sql(query_symbols, conn)

print("\n📍 Most Active Symbols (Asset Concentration):")
print(symbol_stats)



# Check for Data Integrity (Null/Zero Errors)
query_integrity = "SELECT COUNT(*) FROM zerodha_trades WHERE price = 0 OR quantity = 0"
integrity_check = pd.read_sql(query_integrity, conn)

print("\n📍 Data Integrity Audit (Zero/Null Errors):")
print(integrity_check)

conn.close()