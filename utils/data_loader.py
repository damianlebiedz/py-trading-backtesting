import pandas as pd
import backtrader.feeds as btfeeds


def load_data(file_path):
    # Wczytujemy dane z pliku CSV
    data = pd.read_csv(file_path, parse_dates=True, index_col='Date')

    # Konwertujemy dane na format, który Backtrader rozumie
    data_feed = btfeeds.PandasData(dataname=data)

    return data_feed