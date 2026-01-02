"""
Treasury & Hedging Engine:
Aggregates small client orders and calculates the Net Hedge Requirement
to lock in profit spreads.
"""
import pandas as pd

# Simulation of internal customer orders
orders = [
    {'client': 'A', 'type': 'BUY', 'amount_inr': 200},
    {'client': 'B', 'type': 'BUY', 'amount_inr': 15000},
    {'client': 'C', 'type': 'SELL', 'amount_inr': 2000},
    {'client': 'D', 'type': 'BUY', 'amount_inr': 500}
]

df_orders = pd.DataFrame(orders)

# 1. Calculate Net Exposure
total_buys = df_orders[df_orders['type'] == 'BUY']['amount_inr'].sum()
total_sells = df_orders[df_orders['type'] == 'SELL']['amount_inr'].sum()
net_exposure = total_buys - total_sells

# 2. Apply Profit Spread (Procurement Logic)
# If market price is 190,000 and customer price is 200,000
procurement_efficiency = 190000 / 200000  # 0.95
locked_profit = net_exposure * (1 - procurement_efficiency)

print("--- TREASURY HEDGE REPORT ---")
print(f"Total Customer Buys:  ₹{total_buys:,.2f}")
print(f"Total Customer Sells: ₹{total_sells:,.2f}")
print(f"Net Market Hedge Required: ₹{net_exposure:,.2f}")
print(f"Estimated Spread Profit:  ₹{locked_profit:,.2f}")