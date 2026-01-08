import pandas as pd

def should_pause(capital, enabled):
    if not enabled:
        return False, {}

    df = pd.read_csv("logs/trades.csv")
    df = df[df["pnl"].notna()]
    if len(df) < 20:
        return False, {}

    win_rate = (df["pnl"] > 0).mean()
    expectancy = df["pnl"].mean()
    drawdown = (df["pnl"].cumsum().cummax() - df["pnl"].cumsum()).max() / capital

    bad = sum([win_rate < 0.35, expectancy < 0, drawdown > 0.05])

    return bad >= 2, {
        "win_rate": round(win_rate, 2),
        "expectancy": round(expectancy, 2),
        "drawdown": round(drawdown, 3)
    }
