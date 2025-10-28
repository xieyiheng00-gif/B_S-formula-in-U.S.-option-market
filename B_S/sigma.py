from pandas.core.interchange.dataframe_protocol import DataFrame
import numpy as np
from dateutil.relativedelta import relativedelta
import pandas as pd
def get_sigma(current_date,stock_price:DataFrame):
    three_months_before = current_date - relativedelta(months=3)
    stock_price["date"] = pd.to_datetime(stock_price["date"])
    stock_price["date_only"] = stock_price["date"].dt.date
    stock_price = stock_price[
    (stock_price["date_only"] >= three_months_before) &
    (stock_price["date_only"] <= current_date)
]
    stock_price = stock_price.copy()
    stock_price['log_return'] = np.log(stock_price['close'] / stock_price['close'].shift(1))
    sigma = stock_price['log_return'].std() * np.sqrt(252)
    return sigma
