from fyers import fyers

def square_off_all():
    for p in fyers.positions()["netPositions"]:
        if p["qty"] != 0:
            fyers.place_order({
                "symbol": p["symbol"],
                "qty": abs(p["qty"]),
                "type": 2,
                "side": -1 if p["qty"] > 0 else 1,
                "productType": "CNC"
            })
