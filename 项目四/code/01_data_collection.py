import pandas as pd
import random
import os

os.makedirs("../data/ods", exist_ok=True)

platforms = ["淘宝", "京东", "Amazon", "eBay"]
categories = ["按摩仪", "筋膜枪", "护眼仪", "颈椎枕", "足浴盆"]

data = []
for i in range(85000):
    platform = random.choice(platforms)
    category = random.choice(categories)
    price = round(random.uniform(50, 500), 2)
    sales = random.randint(100, 50000)
    comment_count = int(sales * random.uniform(0.05, 0.2))
    rating = round(random.uniform(3.5, 4.9), 1)
    data.append({
        "product_id": i+1,
        "platform": platform,
        "category": category,
        "product_name": f"{category}商品{i}",
        "price": price,
        "monthly_sales": sales,
        "comment_count": comment_count,
        "rating": rating
    })

df = pd.DataFrame(data)
df.to_csv("../data/ods/ods_ecommerce_data.csv", index=False, encoding="utf-8-sig")
print("ODS层电商数据生成完成，共{}条".format(len(df)))
