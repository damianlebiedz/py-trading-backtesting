import backtrader as bt


class BreakoutPreviousDay(bt.Strategy):
    params = (
        ('stop_loss', 0.01),  # Stop loss w procentach
        ('take_profit', 0.02),  # Take profit w procentach
    )

    def __init__(self):
        self.high_previous_day = None
        self.low_previous_day = None

    def next(self):
        # Sprawdzamy, czy mamy dane z poprzedniego dnia
        if len(self.data) < 2:
            return

        # Wyznaczamy max i min z poprzedniego dnia
        if self.data.datetime.date(0) != self.data.datetime.date(-1):
            self.high_previous_day = self.data.high[-1]  # Max z poprzedniego dnia
            self.low_previous_day = self.data.low[-1]  # Min z poprzedniego dnia

        # Wybicie do góry -> Long
        if self.data.close[0] > self.high_previous_day:
            self.buy(size=100)  # Rozmiar pozycji

        # Wybicie do dołu -> Short
        elif self.data.close[0] < self.low_previous_day:
            self.sell(size=100)