import pandas as pd
import os

os.makedirs("../data/dwd", exist_ok=True)

df = pd.read_csv("../data/ods/ods_stock_daily.csv")
df["trade_date"] = pd.to_datetime(df["trade_date"])

# 1. 去重
df = df.drop_duplicates(subset=["stock_code", "trade_date"])

# 2. 缺失值处理：按股票前向填充
df = df.sort_values(["stock_code", "trade_date"])
df[["open", "close", "high", "low", "volume", "turnover"]] = df.groupby("stock_code")[
    ["open", "close", "high", "low", "volume", "turnover"]
].ffill()

# 3. 异常值过滤：涨跌幅±10%限制
df = df[(df["pct_change"] >= -10) & (df["pct_change"] <= 10)]

df.to_csv("../data/dwd/dwd_stock_daily.csv", index=False, encoding="utf-8-sig")
print(f"DWD层清洗完成，有效数据{len(df)}条")
