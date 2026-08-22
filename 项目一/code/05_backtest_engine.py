import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Noto Sans CJK SC', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

os.makedirs("../results", exist_ok=True)

signals = pd.read_csv("../data/ads/ads_top_stocks.csv")
quotes = pd.read_csv("../data/dwd/dwd_stock_daily.csv")

signals["trade_date"] = pd.to_datetime(signals["trade_date"])
quotes["trade_date"] = pd.to_datetime(quotes["trade_date"])

# 合并信号与次日收益
merged = pd.merge(
    signals[["trade_date", "stock_code", "composite_score"]],
    quotes[["trade_date", "stock_code", "pct_change"]],
    on=["trade_date", "stock_code"],
    how="left"
)

# 策略每日收益率（等权重）
daily_return = merged.groupby("trade_date")["pct_change"].mean() / 100

# 计算净值曲线
net_value = (1 + daily_return).cumprod()

# 计算夏普比率
risk_free = 0.03 / 252
excess = daily_return - risk_free
sharpe = np.sqrt(252) * excess.mean() / excess.std()

# 蒙特卡洛模拟1000次
monte_sharpes = []
for _ in range(1000):
    sim_ret = daily_return * np.random.uniform(0.8, 1.2, len(daily_return))
    sim_excess = sim_ret - risk_free
    monte_sharpes.append(np.sqrt(252) * sim_excess.mean() / sim_excess.std())

# 输出结果
with open("../results/backtest_result.txt", "w") as f:
    f.write(f"策略夏普比率: {sharpe:.2f}\n")
    f.write(f"蒙特卡洛模拟1000次平均夏普: {np.mean(monte_sharpes):.2f}\n")
    f.write(f"策略总收益率: {(net_value.iloc[-1] - 1)*100:.2f}%\n")

# 绘制净值曲线
plt.figure(figsize=(10, 5))
plt.plot(net_value.index, net_value.values, label="策略净值")
plt.title("多因子选股策略净值曲线")
plt.legend()
plt.savefig("../results/net_value_curve.png", dpi=150, bbox_inches="tight")
print(f"回测完成，夏普比率: {sharpe:.2f}")
