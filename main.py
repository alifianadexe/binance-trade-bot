from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

from config import user_api

bnb_price = {'error':False}

def bnb_trade_history(msg):
    ''' trade history crypto coin '''
    if msg['e'] != 'error':
        data = msg['k']
        print("Open : {0}   Close : {1}  High : {2} Low : {3}".format(data['o'], data['c'], data['h'], data['l']))
    else:
        print("Error!")        
        
client = Client(user_api.API_KEY, user_api.SECRET_KEY)

bsm  = BinanceSocketManager(client)
conn_key = bsm.start_kline_socket('BNBUSDT', bnb_trade_history)
bsm.start()


