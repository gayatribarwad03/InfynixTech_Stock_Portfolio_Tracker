import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====\n")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish):").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Please choose from thr available stocks.")
        continue

    quantity = int(input("Enter quantity purchased: "))

    investment = stock_prices[stock_name] * quantity

    portfolio[stock_name] = {
        "Quantity": quantity,
        "Price": stock_prices[stock_name],
        "Investment": investment
    }

    total_value = total_value + investment

print("\n===== PORTFOLIO SUMMARY =====\n")

if len(portfolio) == 0:
    print("No stock purchased.")
else:
    for stock, details in portfolio.items():
        print(f"{stock}\n")
        print(f"Price: ${details['Price']}\n")
        print(f"Quantity: {details['Quantity']}\n")
        print(f"Investment: {details['Investment']}\n")
              
        print(f"Total Investment Value = ${total_value}\n")

# Save to TXT file
with open("portfolio_summary.txt","w") as txt_file:
    txt_file.write("STOCK PORTFOLIO SUMMARY\n")
    for stock, details in portfolio.items():
        txt_file.write(f"{stock}\n")
        txt_file.write(f"Price: $ {details['Price']}\n")
        txt_file.write(f"Investment: $ {details['Investment']}\n")
        txt_file.write(f"Total Investment Value = $ {total_value}")

# Save to CSV file
with open ("portfolio_summary.csv","w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Stock","Price","Quantity","Investment"])

    for stock, details in portfolio.items():
        writer.writerow([stock,
                        details["Price"], 
                        details["Quantity"], 
                        details["Investment"]])
        writer.writerow([ ])
        writer.writerow(["Total Investment", total_value])

        print("Portfolio saved successfully!\n")
        print("Files created:")
        print("1. portfolio_summary.txt")
        print("2. portfolio_summary.csv")