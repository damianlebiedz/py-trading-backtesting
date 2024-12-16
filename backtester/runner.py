import backtrader as bt
from utils.data_loader import load_data
from strategies.breakout_range import BreakoutRange
from strategies.breakout_previous_day import BreakoutPreviousDay

def run_backtest(strategy, data_file, cash=10000):
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(cash)  # Ustawiamy początkowy kapitał

    data = load_data(data_file)  # Ładujemy dane
    cerebro.adddata(data)  # Dodajemy dane do backtestera

    cerebro.addstrategy(strategy)  # Dodajemy strategię
    cerebro.run()  # Uruchamiamy backtest

    cerebro.plot()  # Rysujemy wykres wyników