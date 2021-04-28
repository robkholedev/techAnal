import pandas as pd
import os
from iexfinance.stocks import Stock
import mplfinance as mpf

def getOHCLV(ticker):
    results = Stock(ticker, output_format='pandas', token=APIKey)
    dfresults = results.get_time_series()
    return dfresults

pd.set_option('display.max_columns', None)
os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'
APIKey = 'Tpk_03f7cf88a0fb4113bb926a7972472210'
#os.environ['IEX_API_VERSION'] = 'stable'
#APIKey = 'pk_bf5bb7a00fe546e58fc2deeaa254dee5'

ticker = 'PG'

data = getOHCLV(ticker)

#print(data.head())
#mpf.plot(data)