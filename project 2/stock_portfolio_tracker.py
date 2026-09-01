"""
TASK 2: Stock Portfolio Tracker
--------------------------------

Concepts used: dictionary, input/output, basic arithmetic, file handling (optional)
"""

import csv

# Hardcoded stock prices (in your currency of choice)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "INFY": 1600,
    "TCS": 3800,
}


def display_available_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: {price}")


def get_portfolio_from_user():
    """
    Ask the user to enter stock symbols and quantities.
    Returns a dictionary like {"AAPL": 10, "TSLA": 5}.
    """
    portfolio = {}

    print("\nEnter your stock holdings one at a time.")
    print("Type 'done' as the stock symbol when you're finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our price list. Please choose from the list above.")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()

        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity.")
            continue

        quantity = int(qty_input)

        # If the stock is already in the portfolio, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_total_value(portfolio):
    """
    Calculate the value of each holding and the total investment.
    Returns (details_list, total_value).
    """
    details = []
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        details.append((symbol, quantity, price, value))

    return details, total_value


def display_summary(details, total_value):
    print("\n" + "=" * 45)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for symbol, quantity, price, value in details:
        print(f"{symbol:<10}{quantity:<8}{price:<10}{value:<10}")

    print("=" * 45)
    print(f"TOTAL INVESTMENT VALUE: {total_value}")
    print("=" * 45)


def save_to_csv(details, total_value, filename="portfolio_summary.csv"):
    """Optionally save the portfolio summary to a .csv file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])

        for symbol, quantity, price, value in details:
            writer.writerow([symbol, quantity, price, value])

        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total_value])

    print(f"\nSummary saved to '{filename}'.")


def main():
    print("=" * 45)
    print("Stock Portfolio Tracker")
    print("=" * 45)

    display_available_stocks()
    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    details, total_value = calculate_total_value(portfolio)
    display_summary(details, total_value)

    save_choice = input("\nSave this summary to a .csv file? (yes/no): ").lower().strip()
    if save_choice == "yes":
        save_to_csv(details, total_value)


if __name__ == "__main__":
    main()