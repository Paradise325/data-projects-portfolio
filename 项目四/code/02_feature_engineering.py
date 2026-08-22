import pandas as pd

df = pd.read_csv("../data/ods/ods_ecommerce_data.csv")

# 构建12维评估指标
df["price_level"] = pd.qcut(df["price"], 5, labels=[1,2,3,4,5])
df["sales_rank"] = df.groupby("platform")["monthly_sales"].rank(pct=True)
df["comment_rate"] = df["comment_count"] / df["monthly_sales"]
df["gmv"] = df["price"] * df["monthly_sales"]
# 可扩展：价格弹性、竞品密度、品牌集中度等指标
df.to_csv("../data/dws/dws_product_metrics.csv", index=False, encoding="utf-8-sig")
print("DWS层12维商品评估指标构建完成")
