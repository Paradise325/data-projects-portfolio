import pandas as pd
import random
import os

os.makedirs("../../data/ods", exist_ok=True)

industries = ["IT互联网", "制造业", "金融业", "教育", "医疗健康", "房地产", "消费品", "物流"]
cities = ["越城区", "柯桥区", "上虞区", "诸暨市", "嵊州市", "新昌县"]
skills = ["Python", "Java", "SQL", "Excel", "机器学习", "PLC", "CAD", "英语", "会计", "运营"]

data = []
for i in range(52000):
    industry = random.choice(industries)
    city = random.choice(cities)
    salary_min = random.randint(3, 25)
    salary_max = salary_min + random.randint(2, 10)
    exp = random.choice(["应届生", "1-3年", "3-5年", "5-10年"])
    skill = random.sample(skills, random.randint(2, 5))
    data.append({
        "job_id": i+1,
        "job_name": f"{industry}岗位{i}",
        "industry": industry,
        "city": city,
        "salary_min": salary_min,
        "salary_max": salary_max,
        "experience": exp,
        "skills": ",".join(skill),
        "company": f"企业{i}"
    })

df = pd.DataFrame(data)
df.to_csv("../../data/ods/ods_recruitment_data.csv", index=False, encoding="utf-8-sig")
print("ODS层招聘数据生成完成，共{}条".format(len(df)))
