import pandas as pd
from datetime import datetime, timedelta
from fyers import fyers
from adaptive_thresholds import compute

BASE = [
    "IOC","BPCL","GAIL","SAIL","NMDC","COALINDIA",
    "PNB","UNIONBANK","CANBK","IRFC","RVNL",
    "NHPC","NBCC","HUDCO","TATAPOWER","ADANIPOWER","MRPL"
]

to_date = datetime.now()
from_date = to_date - timedelta(days=20)

rows = []

for s in BASE:
    try:
        d = fyers.history({
            "symbol": f"NSE:{s}-EQ",
            "resolution": "D",
            "date_format": "1",
            "range_from": from_date.strftime("%Y-%m-%d"),
            "range_to": to_date.strftime("%Y-%m-%d")
        })
        df = pd.DataFrame(d["candles"], columns=["t","o","h","l","c","v"]).tail(10)
        atr = (df["h"] - df["l"]).mean()
        rows.append({
            "symbol": s,
            "price": df["c"].iloc[-1],
            "avg_volume": df["v"].mean(),
            "atr_pct": (atr / df["c"].iloc[-1]) * 100,
            "gap_pct": abs((df["o"].iloc[-1] - df["c"].iloc[-2]) / df["c"].iloc[-2]) * 100
        })
    except:
        pass

raw = pd.DataFrame(rows)
vol_t, atr_t = compute(raw)

raw = raw[(raw["price"] < 200) &
          (raw["avg_volume"] > vol_t) &
          (raw["atr_pct"] > atr_t)]

raw["score"] = (
    raw["avg_volume"]/vol_t * 0.4 +
    raw["atr_pct"] * 0.4 +
    raw["gap_pct"] * 0.2
)

print(raw.sort_values("score", ascending=False).head(3))
