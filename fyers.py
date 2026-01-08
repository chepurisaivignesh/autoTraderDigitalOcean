from fyers_apiv3 import fyersModel
from fyers_auth import authenticate
from config import APP_ID

fyers = fyersModel.FyersModel(
    client_id=APP_ID,
    token=authenticate(),
    log_path="logs/"
)

def place_order(symbol, action, qty):
    return fyers.place_order({
        "symbol": f"NSE:{symbol}-EQ",
        "qty": qty,
        "type": 2,
        "side": 1 if action == "BUY" else -1,
        "productType": "CNC",
        "validity": "DAY"
    })
