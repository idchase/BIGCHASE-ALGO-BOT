class TradingBot:
    def __init__(self):
        self.portfolio = {}
        self.balance = 10000  # Initial balance

    def execute_trade(self, symbol, amount, price):
        cost = amount * price
        if cost > self.balance:
            print(f'Insufficient balance to execute trade for {symbol}.')
            return False
        self.balance -= cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount
        print(f'Trade executed: {amount} of {symbol} at ${price} each.')
        return True

    def manage_portfolio(self):
        # Add logic here to manage portfolio, e.g., rebalancing
        print('Managing portfolio...')

    def show_portfolio(self):
        print('Current portfolio:')
        for symbol, amount in self.portfolio.items():
            print(f'{symbol}: {amount}')
        print(f'Balance: ${self.balance}')

if __name__ == '__main__':
    bot = TradingBot()
    bot.execute_trade('AAPL', 5, 150)
    bot.show_portfolio()