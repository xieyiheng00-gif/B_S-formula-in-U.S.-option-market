import B_S
import gain_data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

def get_option_price_through_formula(stock_name:str="AAPL",strike_price:int=245,start_date="2025-01-01",
                                     strike_date:str="2026-02-20",call_or_put:str='call'):
    data_stock=gain_data.gain_stock_data_per_day_2025(stock_name,start_date,"2025-12-31")
    data_option_call=gain_data.gain_option_data_per_day_2025(stock_name,strike_date,strike_price,call_or_put=call_or_put)
    data_option_put=gain_data.gain_option_data_per_day_2025(stock_name,strike_date,strike_price,call_or_put=call_or_put)

    current_date=data_option_call['date'].min().date()
    today_date=datetime.today().date()
    ans = [[]]
    while current_date < today_date :
        ans.append(B_S.black_scholes(data_stock,current_date,strike_date,strike_price,0.04,option_type=call_or_put))
        current_date += timedelta(days=1)

    ans=[x for x in ans if x != [0]]
    ans=pd.DataFrame(ans)
    ans=pd.concat([data_option_call,ans],axis=1)
    ans=pd.concat([data_stock,ans],axis=1)
    return(ans)




a=get_option_price_through_formula("NVDA",185)


