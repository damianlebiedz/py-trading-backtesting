from backtester.runner import run_backtest
from strategies.breakout_range import BreakoutRange
from strategies.breakout_previous_day import BreakoutPreviousDay

if __name__ == '__main__':
    data_file = 'data/sp500.csv'
    run_backtest(BreakoutRange, data_file)
    run_backtest(BreakoutPreviousDay, data_file)