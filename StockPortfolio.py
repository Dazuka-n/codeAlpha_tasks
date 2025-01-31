import yfinance as yf
from tabulate import tabulate

# Portfolio Dictionary
portfolio = {}

def add_stock(ticker, quantity, purchase_price):
    """Add a stock to the portfolio."""
    portfolio[ticker.upper()] = {
        "quantity": quantity,
        "purchase_price": purchase_price
    }
    print(f"Added {quantity} shares of {ticker} at ${purchase_price} per share.")

def remove_stock(ticker):
    """Remove a stock from the portfolio."""
    ticker = ticker.upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from the portfolio.")
    else:
        print(f"{ticker} not found in the portfolio.")

def get_stock_data(ticker):
    """Fetch real-time stock data."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        return data['Close'].iloc[-1]
    else:
        print(f"Failed to fetch data for {ticker}.")
        return None

def view_portfolio():
    """View the portfolio with real-time performance data."""
    if not portfolio:
        print("Portfolio is empty.")
        return

    table = []
    total_investment = 0
    total_current_value = 0

    for ticker, info in portfolio.items():
        current_price = get_stock_data(ticker)
        if current_price is None:
            continue
        
        quantity = info["quantity"]
        purchase_price = info["purchase_price"]
        current_value = quantity * current_price
        investment = quantity * purchase_price
        profit_loss = current_value - investment
        profit_loss_percent = (profit_loss / investment) * 100

        total_investment += investment
        total_current_value += current_value

        table.append([
            ticker,
            quantity,
            f"${purchase_price:.2f}",
            f"${current_price:.2f}",
            f"${current_value:.2f}",
            f"${profit_loss:.2f}",
            f"{profit_loss_percent:.2f}%"
        ])

    print(tabulate(
        table,
        headers=["Ticker", "Quantity", "Purchase Price", "Current Price", "Current Value", "Profit/Loss ($)", "Profit/Loss (%)"],
        tablefmt="grid"
    ))
    print(f"\nTotal Investment: ${total_investment:.2f}")
    print(f"Total Current Value: ${total_current_value:.2f}")
    print(f"Overall Profit/Loss: ${total_current_value - total_investment:.2f}")

# Example Usage
if __name__ == "__main__":
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker: ").strip()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(ticker, quantity, purchase_price)

        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").strip()
            remove_stock(ticker)

        elif choice == "3":
            view_portfolio()

        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")