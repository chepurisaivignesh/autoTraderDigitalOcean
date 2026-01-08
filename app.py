from flask import Flask, request
import threading
from fyers import place_order
from risk import allow_trade, register_trade
from scheduler import auto_exit_loop
from self_diagnosis import should_pause
from logger import log
from config import CAPITAL, TRADE_VALUE, AUTO_PAUSE_ENABLED, KILL_SWITCH

app = Flask(__name__)
threading.Thread(target=auto_exit_loop, daemon=True).start()

@app.route("/webhook", methods=["POST"])
def webhook():
    if KILL_SWITCH:
        return {"status":"killed"}

    d = request.json
    symbol, action, price = d["symbol"], d["action"], float(d["price"])

    pause, diag = should_pause(CAPITAL, AUTO_PAUSE_ENABLED)
    if pause:
        return {"status":"paused","diag":diag}

    log("signals.csv",[symbol,action,price])

    if not allow_trade(symbol):
        return {"status":"blocked"}

    qty = int(TRADE_VALUE / price)
    place_order(symbol, action, qty)
    register_trade(symbol)

    log("trades.csv",[symbol,action,qty,"PLACED"])
    return {"status":"ok"}

app.run(host="0.0.0.0", port=5000)
