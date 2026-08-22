
---

### 项目三：绍兴市就业市场供需失衡分析与数据洞察
# 绍兴市就业市场供需失衡分析与数据洞察

## 项目描述
针对绍兴市就业市场结构性供需错配问题，搭建招聘行业数据采集、数仓建设、多维分析到可视化交付的全链路数据平台。按 ODS/DWD/DWS/ADS 四层架构完成数据集市建设，设计15+核心指标的综合评估体系，定量识别供需失衡的核心驱动因素，最终输出数据洞察报告与交互式可视化驾驶舱，为校方专业设置论证提供数据支撑。

## 技术栈
Python、MySQL、SQL（复杂查询/窗口函数/性能调优）、多线程爬虫、数据仓库ODS/DWD/DWS/ADS分层建模、离线ETL加工、数据标准化治理、Power BI可视化、ECharts

## 目录结构
├── code/
│   ├── 01_ods_sim_data.py       # ODS 层模拟招聘数据生成
│   ├── 02_dwd_data_clean.py     # DWD 层数据清洗与字段拆分
│   ├── 03_dws_aggregation.py    # DWS 层多维聚合计算
│   └── 04_ads_mismatch_index.py # ADS 层供需失衡指标计算
├── sql/
│   └── create_tables.sql        # 数仓四层建表 SQL 语句
├── data/
│   ├── ods/dwd/ dws/ads/      # 各层数据文件
├── powerbi/
│   └── 人才市场数据驾驶舱.pbix # Power BI 交互式看板
└── results/                     # 分析报告、结论文档

## 运行步骤
### 1. 环境依赖
```bash
pip install pandas numpy pymysql sqlalchemy
执行 `sql/create_tables.sql` 脚本，在 MySQL 中创建 ODS/DWD/DWS/ADS 四层数据表。

依次运行 code 目录下的 01-04 号脚本，完成从原始数据生成到失衡指标计算的全流程：
python code/01_ods_sim_data.py
python code/02_dwd_data_clean.py
python code/03_dws_aggregation.py
python code/04_ads_mismatch_index.py

