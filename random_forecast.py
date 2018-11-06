import numpy as np
import pandas as pd
import quandl  # Necessary for obtaining financial data easily
from backtest import Strategy, Portfolio


class RandomForecastingStrategy(Strategy):
    """Derives from Strategy to produce a set of signals that
        are randomly generated long/shorts. Clearly a nonsensical
        strategy, but perfectly acceptable for demonstrating the
        backtesting infrastructure!"""

    def __init__(self, symbol, bars):
        self.symbol = symbol
        self.bars = bars

    def generate_signals(self):
        """Creates a pandas DataFrame of random signals."""
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = np.sign(np.random.rand(len(signals)))

        # The first five elements are set to zero in order to minimise
        # upstream NaN errors in the forecaster.
        signals['signal'][0:5] = 0.0
        return signals


class MarketOnOpenPortfolio(Portfolio):
