import pandas as pd
import sqlite3
import os

# 1. Path Setup
base_path = os.path.dirname(os.path.abspath(__file__))
# We will migrate your Zerodha Commodity data (₹18.2 Cr)
zerodha_path = os.path.join(base_path, '..', 'data', 'tradebook-CLS535-COM (1).csv')
db_path = os.path.join(base_path, '..', 'data', 'trading_vault.db')

try:
    # 2. Load the Institutional Dataset
    df = pd.read_csv(zerodha_path)
    
    # 3. Connect to the SQL Engine
    conn = sqlite3.connect(db_path)
    
    # 4. Create the Table
    df.to_sql('zerodha_trades', conn, if_exists='replace', index=False)
    
    print("✅ Migration Successful!")
    print(f"📂 Database created at: {db_path}")
    
    # 5. Verification: Count the records in the Vault
    count = pd.read_sql("SELECT COUNT(*) FROM zerodha_trades", conn).iloc[0,0]
    print(f"📊 Total Records in SQL Vault: {count}")
    
    conn.close()

except Exception as e:
    print(f"❌ Migration Failed: {e}")