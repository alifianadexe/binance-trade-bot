from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

from config import user_api

import pandas as pd
import json
import csv

bnb_price = {'error':False}

def bnb_trade_history(msg):
    ''' trade history crypto coin '''
    if msg['e'] != 'error':
        data = msg['k']
        print("Open : {0}   Close : {1}  High : {2} Low : {3}".format(data['o'], data['c'], data['h'], data['l']))
    else:
        print("Error!")        
        
client = Client(user_api.API_KEY, user_api.SECRET_KEY)

# open the websocket
# bsm  = BinanceSocketManager(client)
# conn_key = bsm.start_kline_socket('BNBUSDT', bnb_trade_history)
# bsm.start()


# valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

# get timestamp of earliest date data availabel
timestamp = client._get_earliest_valid_timestamp('BNBUSDT', '1d')
print(timestamp)

bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit=1000)

# delete unwanted data
for line in bars:
    del line[5:]

bnb_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
bnb_df.set_index('date', inplace=True)
print(bnb_df.head())




