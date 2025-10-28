import numpy as np
from scipy.stats import norm
from pandas.core.interchange.dataframe_protocol import DataFrame
from datetime import datetime
from sigma import get_sigma
import time_compute
import pandas as pd
def black_scholes(stock_price:DataFrame, date, strike_date:str, Strike_price, r, q=0.0, option_type='call'):
    """
    Black-Scholes option pricing formula.
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate (annual)
    sigma : float
        Volatility of the underlying (annual)
    q : float, optional
        Dividend yield (annual, default=0)
    option_type : str, 'call' or 'put'
        Option type

    price : float
        Theoretical option price
    """
    sigma=get_sigma(date,stock_price)
    T=time_compute.compute_date_to_strike(date,strike_date)
    T=T/365
    stock_price["date"] = pd.to_datetime(stock_price["date"])
    stock_price["date"] = stock_price["date"].dt.date
    if date in stock_price['date'].values:
        S = stock_price.loc[stock_price['date'] == date, 'close'].values[0]
    else:
        return [0]
    if T <= 0 or sigma <= 0:
        # Handle expiry or zero-vol cases
        if option_type == 'call':
            return max(S - Strike_price, 0)
        else:
            return max(Strike_price - S, 0)

    d1 = (np.log(S / Strike_price) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * np.exp(-q * T) * norm.cdf(d1) - Strike_price * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = Strike_price * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    price=[price,S,Strike_price,sigma,T]
    return price








# def bs_greeks(S, K, T, r, sigma, q=0.0):
#     d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
#     d2 = d1 - sigma * np.sqrt(T)
#
#     delta_call = np.exp(-q * T) * norm.cdf(d1)
#     delta_put = np.exp(-q * T) * (norm.cdf(d1) - 1)
#     gamma = np.exp(-q * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
#     vega = S * np.exp(-q * T) * norm.pdf(d1) * np.sqrt(T)
#     theta_call = (-S * np.exp(-q * T) * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
#                   - r * K * np.exp(-r * T) * norm.cdf(d2)
#                   + q * S * np.exp(-q * T) * norm.cdf(d1))
#     theta_put = (-S * np.exp(-q * T) * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
#                  + r * K * np.exp(-r * T) * norm.cdf(-d2)
#                  - q * S * np.exp(-q * T) * norm.cdf(-d1))
#
#     return {
#         "Delta(Call)": delta_call,
#         "Delta(Put)": delta_put,
#         "Gamma": gamma,
#         "Vega": vega,
#         "Theta(Call)": theta_call,
#         "Theta(Put)": theta_put
#     }
#
#





