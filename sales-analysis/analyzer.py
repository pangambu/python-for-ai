import pandas as pd
from helpers import calculate_total, format_currency

# Read data 
df = pd.read_csv("sales-analysis/data/sales.csv")

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row["Quantity"], row["Price"])
    totals.append(total)

# Add totals to our data
df["Total"] = totals

# Display with formatted totals
print("Sales Data")
for index, row in df.iterrows():
    formatted_total = format_currency(row["Total"])
    print(f"Item: {row['Product']} : {formatted_total}")

# Show grand total
grand_total = df["Total"].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")
