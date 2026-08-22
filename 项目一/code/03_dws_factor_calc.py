import pandas as pd
import os

os.makedirs("../data/dws", exist_ok=True)

df = pd.read_csv("../data/dwd/dwd_stock_daily.csv")
df["trade_date"] = pd.to_datetime(df["trade_date"])
df = df.sort_values(["stock_code", "trade_date"])

def calc_factors(group):
    group["stock_code"] = group.name

    # 动量因子
    group["momentum_5d"] = group["close"].pct_change(5)
    group["momentum_20d"] = group["close"].pct_change(20)
    # 波动率因子
    group["volatility_5d"] = group["pct_change"].rolling(5).std()
    group["volatility_20d"] = group["pct_change"].rolling(20).std()
    # 流动性因子
    group["liquidity_20d"] = group["turnover"].rolling(20).mean()
    # 反转因子
    group["reverse_5d"] = -group["close"].pct_change(5)
    return group

df = df.groupby("stock_code", group_keys=False).apply(calc_factors, include_groups=False)
df = df.dropna()

df.to_csv("../data/dws/dws_factor_daily.csv", index=False, encoding="utf-8-sig")
print("DWS层6大类因子计算完成")