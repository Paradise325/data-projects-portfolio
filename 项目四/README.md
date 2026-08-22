
---

### 项目四：跨境电商选品决策数据洞察与市场机会挖掘
```markdown
# 跨境电商选品决策数据洞察与市场机会挖掘

## 项目描述
面向跨境电商选品业务场景，搭建国内外多平台电商数据整合分析平台。覆盖商品数据采集、跨平台数据对齐、特征工程、销量预测到机会评分的全流程，构建12维商品评估指标体系，结合时序预测与情感分析算法输出量化的市场机会评分，为选品决策与营销策略制定提供数据驱动的支撑。

## 技术栈
Python、SQL、Prophet时序预测、SnowNLP情感分析、多源数据集成、数据仓库ODS/DWD/DWS/ADS分层建模、特征工程、市场机会评分模型、ECharts数据可视化

## 目录结构
├── code/
│   ├── 01_ods_sim_data.py           # ODS 层跨平台模拟数据生成
│   ├── 02_dwd_data_clean.py         # DWD 层数据标准化与清洗
│   ├── 03_dws_feature_engineering.py# DWS 层 12 维评估指标构建
│   ├── 04_forecast_sentiment.py     # 销量预测与评论情感分析
│   └── 05_opportunity_score.py      # 市场机会综合评分模型
├── data/
│   ├── ods/dwd/ dws/               # 各层数据文件
└── results/                         # 预测结果、潜力单品清单、分析报告

## 运行步骤
### 1. 环境依赖
```bash
pip install pandas numpy prophet snownlp matplotlib

依次运行 code 目录下的脚本，完成从数据生成到机会评分的完整链路：
# 1. 生成多平台模拟商品数据
python code/01_ods_sim_data.py

# 2. 跨平台数据标准化清洗
python code/02_dwd_data_clean.py

# 3. 构建12维商品评估指标
python code/03_dws_feature_engineering.py

# 4. 销量时序预测 + 评论情感分析
python code/04_forecast_sentiment.py

# 5. 市场机会综合评分与潜力单品筛选
python code/05_opportunity_score.py
