import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:你的密码@localhost:3306/shaoxing_job_market")

# 1. ODS数据写入
df = pd.read_csv("../../data/ods/ods_recruitment_data.csv")
df.to_sql("ods_recruitment", engine, if_exists="replace", index=False)

# 2. DWD层：字段拆分与清洗
dwd_sql = """
INSERT INTO dwd_recruitment_clean
SELECT 
    job_id,
    job_name,
    industry,
    city,
    (salary_min + salary_max)/2 as salary_avg,
    experience,
    SUBSTRING_INDEX(SUBSTRING_INDEX(skills, ',', n), ',', -1) as skill_word,
    company
FROM ods_recruitment
JOIN (SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5) nums
WHERE n <= LENGTH(skills)-LENGTH(REPLACE(skills, ',', '')) + 1
"""
with engine.connect() as conn:
    conn.execute(dwd_sql)

# 3. DWS层：多维聚合
dws_sql = """
INSERT INTO dws_industry_city_summary
SELECT industry, city, COUNT(DISTINCT job_id) as job_count, AVG(salary_avg) as avg_salary
FROM dwd_recruitment_clean
GROUP BY industry, city
"""
with engine.connect() as conn:
    conn.execute(dws_sql)

# 4. ADS层：供需失衡指标
ads_sql = """
INSERT INTO ads_supply_demand_index
SELECT 
    industry,
    job_count as demand_score,
    ROUND(job_count * 0.6, 0) as supply_score,
    ROUND(job_count * 0.4 / job_count, 2) as mismatch_ratio
FROM dws_industry_city_summary
GROUP BY industry
"""
with engine.connect() as conn:
    conn.execute(ads_sql)

print("ETL全流程执行完成，数仓四层数据已落地")
