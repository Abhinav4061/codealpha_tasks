import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140,
    "NFLX": 450
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive!")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Add quantity if stock already exists
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    choice = input("Add another stock? (y/n): ").lower()
    if choice != 'y':
        break

# Display portfolio
print("\n" + "=" * 55)
print("{:<10}{:<10}{:<15}{:<15}".format(
    "Stock", "Qty", "Price($)", "Value($)"
))
print("=" * 55)

for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value

    print("{:<10}{:<10}{:<15}{:<15}".format(
        stock, qty, stock_prices[stock], value
    ))

print("=" * 55)
print(f"Total Portfolio Value: ${total_investment}")

# Find highest investment stock
highest_stock = max(
    portfolio,
    key=lambda x: portfolio[x] * stock_prices[x]
)

highest_value = portfolio[highest_stock] * stock_prices[highest_stock]

print(f"Highest Investment: {highest_stock} (${highest_value})")

# Save to CSV file
save = input("\nSave portfolio to CSV file? (y/n): ").lower()

if save == 'y':
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            writer.writerow([stock, qty, stock_prices[stock], value])

        writer.writerow([])
        writer.writerow(["Total Portfolio Value", total_investment])

    print("Portfolio saved successfully as 'portfolio.csv'")

print("\nThank you for using Stock Portfolio Tracker!")
