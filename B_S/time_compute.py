from datetime import datetime

def convert_strike_date_to_ticker_format(time:str="2026-01-16"):
    yy=time[2:4]
    mm=time[5:7]
    dd=time[8:10]
    return f"{yy}{mm}{dd}"


def compute_date_to_strike(date,strike_date="2026-01-16"):
    strike_date=datetime.strptime(strike_date,"%Y-%m-%d")
    strike_date=strike_date.date()
    return (strike_date - date).days
