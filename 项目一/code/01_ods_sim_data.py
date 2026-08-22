import pandas as pd
import numpy as np
import os

os.makedirs("../data/ods", exist_ok=True)

# 模拟100只股票池
stock_codes = [f"{i:06d}" for i in range(1, 101)]
dates = pd.date_range(start="2020-01-02", end="2025-11-30", freq="B")

all_data = []
np.random.seed(42)

for code in stock_codes:
    # 生成带趋势的价格序列
    base_price = np.random.uniform(5, 50)
    daily_return = np.random.normal(0.0003, 0.02, len(dates))
    price = base_price * np.cumprod(1 + daily_return)

    # 生成成交量、换手率
    volume = np.random.randint(100000, 10000000, len(dates))
    turnover = np.random.uniform(0.5, 10, len(dates))

    df = pd.DataFrame({
        "trade_date": dates,
        "stock_code": code,
        "open": price * np.random.uniform(0.98, 1.02, len(dates)),
        "close": price,
        "high": price * np.random.uniform(1.0, 1.03, len(dates)),
        "low": price * np.random.uniform(0.97, 1.0, len(dates)),
        "volume": volume,
        "turnover": turnover,
        "pct_change": daily_return * 100
    })
    all_data.append(df)

ods_data = pd.concat(all_data, ignore_index=True)
ods_data.to_csv("../data/ods/ods_stock_daily.csv", index=False, encoding="utf-8-sig")
print(f"ODS层模拟数据生成完成，共{len(ods_data)}条记录，覆盖100只股票")
