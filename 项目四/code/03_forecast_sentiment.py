import pandas as pd
import numpy as np
from prophet import Prophet
from snownlp import SnowNLP

# 1. Prophet时序销量预测
dates = pd.date_range(start="2023-01-01", end="2024-05-01", freq="D")
sales_data = pd.DataFrame({
    "ds": dates,
    "y": [100 + i*0.5 + 20*np.sin(i/30) for i in range(len(dates))]
})

model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.fit(sales_data)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)
forecast.to_csv("../results/sales_forecast.csv", index=False)
print("销量预测完成，预测未来90天趋势")

# 2. SnowNLP评论情感分析
sample_comments = [
    "质量很好，用着很舒服",
    "效果一般，不值这个价",
    "物流很快，客服态度好",
    "噪音有点大，其他还行"
]
sentiments = [SnowNLP(c).sentiments for c in sample_comments]
print(f"平均情感指数: {np.mean(sentiments):.2f}")
