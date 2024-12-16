import backtrader as bt


class BreakoutRange(bt.Strategy):
    params = (
        ('range_hours', 1),  # Liczba godzin przed otwarciem do wyznaczenia zakresu
        ('stop_loss', 0.01),  # Stop loss w procentach
        ('take_profit', 0.02),  # Take profit w procentach
    )

    def __init__(self):
        self.high_range = None
        self.low_range = None

    def next(self):
        # Sprawdzamy czy mamy wystarczającą ilość danych (np. 1 godzinę przed sesją)
        if len(self.data) < self.params.range_hours * 60:
            return

        # Wyznaczamy max i min w zakresie godziny przed otwarciem
        if not self.high_range:
            self.high_range = max(self.data.high.get(size=self.params.range_hours * 60))
            self.low_range = min(self.data.low.get(size=self.params.range_hours * 60))

        # Wybicie do góry -> Long
        if self.data.close[0] > self.high_range:
            self.buy(size=100)  # Domyślny rozmiar pozycji

        # Wybicie do dołu -> Short
        elif self.data.close[0] < self.low_range:
            self.sell(size=100)