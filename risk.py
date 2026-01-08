from datetime import datetime
from config import MAX_TRADES, MAX_LOSS

trades = 0
loss = 0
symbols = set()

def allow_trade(symbol):
    global trades, loss
    if trades >= MAX_TRADES or loss <= MAX_LOSS:
        return False
    if symbol in symbols:
        return False
    if datetime.now().strftime("%H:%M") >= "15:00":
        return False
    return True

def register_trade(symbol):
    global trades
    trades += 1
    symbols.add(symbol)
