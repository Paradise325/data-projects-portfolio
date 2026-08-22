import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

os.makedirs("../data/ads", exist_ok=True)

df = pd.read_csv("../data/dws/dws_factor_daily.csv")

factor_cols = ["momentum_20d", "volatility_20d", "liquidity_20d", "reverse_5d"]
scaler = StandardScaler()
df[factor_cols] = scaler.fit_transform(df[factor_cols])

# 加权综合评分
weights = {
    "momentum_20d": 0.3,
    "volatility_20d": -0.2,
    "liquidity_20d": 0.2,
    "reverse_5d": 0.3
}
df["composite_score"] = sum(df[col] * w for col, w in weights.items())

# 每日选出评分前10的股票
top_stocks = df.sort_values(["trade_date", "composite_score"], ascending=[True, False])\
               .groupby("trade_date").head(10)

top_stocks.to_csv("../data/ads/ads_top_stocks.csv", index=False, encoding="utf-8-sig")
print("ADS层综合评分计算完成，每日Top10股票池已生成")
