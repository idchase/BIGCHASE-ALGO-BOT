# Complete Trading Bot Entry Point

# Importing necessary modules
from config import Config
from bot import Bot
from strategy import Strategy
from data_handler import DataHandler

# Main entry point for the trading bot
if __name__ == '__main__':
    # Initialize config
    config = Config()

    # Initialize data handler with config settings
    data_handler = DataHandler(config)

    # Initialize strategy
    strategy = Strategy(config)

    # Initialize bot with strategy and data handler
    bot = Bot(strategy, data_handler)

    # Execute the trading bot
    bot.run()