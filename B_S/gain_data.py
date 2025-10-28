import requests
import pandas as pd
from datetime import datetime
def gain_option_data_per_day_2025(option_name:str,strike_date:str,strike_price:int=245,call_or_put:str='call'):
    #not robust, need to write a function to convert date to right format.
    #stike_data "260220"
    strike_date=datetime.strptime(strike_date,"%Y-%m-%d")
    strike_date=strike_date.strftime("%y%m%d")
    api_key = "api_key"
    if call_or_put=='call':
        call_or_put="C"
    elif call_or_put=='put':
        call_or_put="P"
    else:
        print("Call or Put error")
        return
    strike_price = f"{int(strike_price * 1000):08d}"
    symbol = "O:"+option_name+strike_date+call_or_put+strike_price  # AAPL call, strike=175, expiry=2024-06-21
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2025-01-01/2025-12-31?apiKey={api_key}"

    r = requests.get(url)
    data = r.json()['results']

    df = pd.DataFrame(data)
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    df = df[['t', 'o', 'h', 'l', 'c', 'v']]
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

    return df


def gain_stock_data_per_day_2025(stock_name:str,start_date:str="2025-01-01",end_date:str="2025-12-31"):
    api_key = "api_key"
    start_date=datetime.strptime(start_date,"%Y-%m-%d")
    start_date=start_date.strftime("%Y-%m-%d")
    end_date=datetime.strptime(end_date,"%Y-%m-%d")
    end_date=end_date.strftime("%Y-%m-%d")
    url=f"https://api.polygon.io/v2/aggs/ticker/{stock_name}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={api_key}"
    r = requests.get(url)
    data = r.json()['results']

    df = pd.DataFrame(data)
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    df = df[['t', 'o', 'h', 'l', 'c', 'v','vw']]
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume','volume weighted average price']

    return df
