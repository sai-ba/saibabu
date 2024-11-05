import requests

class Stock:
    def __init__(self, symbol, quantity):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.current_price = 0.0
        self.total_value = 0.0

    def update_price(self, api_key):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={self.symbol}&interval=5min&apikey={api_key}'
        response = requests.get(url)
        data = response.json()

        try:
            latest_price = float(next(iter(data['Time Series (5min)'].values()))['1. open'])
            self.current_price = latest_price
            self.total_value = self.quantity * self.current_price
        except KeyError:
            print(f"Error retrieving data for {self.symbol}")

class Portfolio:
    def __init__(self):
        self.stocks = {}
        self.api_key = 'YOUR_API_KEY'

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity += quantity
        else:
            self.stocks[symbol] = Stock(symbol, quantity)
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"{symbol} not found in portfolio.")

    def update_portfolio(self):
        for stock in self.stocks.values():
            stock.update_price(self.api_key)

    def view_portfolio(self):
        print("\nPortfolio:")
        total_portfolio_value = 0
        for stock in self.stocks.values():
            stock.update_price(self.api_key)
            total_portfolio_value += stock.total_value
            print(f"{stock.symbol}: {stock.quantity} shares at ${stock.current_price:.2f} each, Total Value: ${stock.total_value:.2f}")
        print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

    def track(self):
        while True:
            action = input("\nChoose an action: (add, remove, view, exit): ").lower()
            if action == 'add':
                symbol = input("Enter stock symbol: ").upper()
                quantity = int(input("Enter quantity of shares: "))
                self.add_stock(symbol, quantity)
            elif action == 'remove':
                symbol = input("Enter stock symbol to remove: ").upper()
                self.remove_stock(symbol)
            elif action == 'view':
                self.view_portfolio()
            elif action == 'exit':
                break
            else:
                print("Invalid action. Please try again.")

# Usage
portfolio = Portfolio()
portfolio.track()
