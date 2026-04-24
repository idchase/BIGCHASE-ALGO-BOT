import pandas as pd
import numpy as np

class TechnicalAnalysis:
    def __init__(self, data):
        self.data = data

    def moving_average(self, window):
        return self.data['Close'].rolling(window=window).mean()

    def buy_signal(self, short_window, long_window):
        signals = np.where(self.moving_average(short_window) > self.moving_average(long_window), 1, 0)
        return signals

    def sell_signal(self, short_window, long_window):
        signals = np.where(self.moving_average(short_window) < self.moving_average(long_window), -1, 0)
        return signals

    def generate_signals(self, short_window, long_window):
        buy_signals = self.buy_signal(short_window, long_window)
        sell_signals = self.sell_signal(short_window, long_window)
        combined_signals = buy_signals + sell_signals
        return combined_signals

# Example usage
# df = pd.read_csv('your_data.csv')  # Ensure to load your market data
# ta = TechnicalAnalysis(df)
# signals = ta.generate_signals(short_window=50, long_window=200)  # Short and long window for moving averages