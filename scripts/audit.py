import pandas as pd

# Load your specific Exness data
# Adjust filename if your sub-folder path is different
file_path = 'data\\01_01_2007-23_12_2025 (1).csv'

try:
    df = pd.read_csv(file_path)
    # Fix the date issue we found earlier
    df['opening_time_utc'] = pd.to_datetime(df['opening_time_utc'], format='mixed')
    
    print("--- RAW DATA AUDIT ---")
    print(f"Total Transactions Found: {len(df)}")
    print(f"Total Profit/Loss: ${df['profit_usd'].sum():,.2f}")
    
    # Let's find your largest single trade
    max_win = df['profit_usd'].max()
    max_loss = df['profit_usd'].min()
    
    print(f"Largest Win: ${max_win:,.2f}")
    print(f"Largest Loss: ${max_loss:,.2f}")

except Exception as e:
    print(f"Error loading data: {e}")