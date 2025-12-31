
"""
Domestic Portfolio Integration:
Parses and cleans tradebook data for the Indian Commodity Market (MCX).
Standardizes execution logs for migration into the centralized SQL Risk Vault.
"""# Mapping your Real-Money Zerodha Turnover to Business Segments
zerodha_portfolio = {
    "MCX_Commodity": 181955053.50, # approx ₹18.2 Cr
    "NSE_FO": 2113641.25,          # approx ₹21 Lakhs
    "Total_Turnover": 184068694.75 # Total ₹18.4 Cr
}

# Demonstrating Dictionary Access (Senior Data Analyst Skill)
for segment, value in zerodha_portfolio.items():
    print(f"Segment: {segment} | Managed Capital: ₹{value:,.2f}")

# Supercoach Check: Extract the specific Commodity value
print(f"\nTargeting Commodity Volatility for: ₹{zerodha_portfolio['MCX_Commodity']:,.2f}")