import numpy as np

def compute(df):
    vol = max(np.percentile(df["avg_volume"], 70), 500_000)
    atr = max(np.percentile(df["atr_pct"], 60), 0.8)
    return vol, atr
