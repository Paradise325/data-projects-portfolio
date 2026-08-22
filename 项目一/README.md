# 基于多因子模型的A股量化选股策略构建与回测

## 项目描述
面向量化投研场景，搭建A股多因子选股全链路数据处理与回测体系，覆盖多源市场数据接入、数仓分层建模、因子批量计算到策略回测验证的完整流程，支撑量化策略的快速迭代与风险收益量化评估。

## 技术栈
Python、SQL（窗口函数/复杂查询）、数据仓库ODS/DWD/DWS/ADS分层、离线ETL、Pandas/NumPy、蒙特卡洛模拟、Power BI可视化

## 目录结构
├── code/      # 核心代码
│   ├── 01_ods_sim_data.py       # ODS 层模拟数据生成
│   ├── 02_dwd_data_clean.py     # DWD 层数据清洗
│   ├── 03_dws_factor_calc.py    # DWS 层因子计算
│   ├── 04_ads_score_calc.py     # ADS 层综合评分
│   └── 05_backtest_engine.py    # 回测引擎
├── data/     # 分层数据
│   ├── ods/dwd/ dws/ads/
├── powerbi/  # Power BI 可视化看板
└── results/  # 回测结果与图表

## 运行步骤
1. 安装依赖：`pip install pandas numpy matplotlib scikit-learn`
2. 依次运行 code 目录下的 01-05 号脚本
3. 打开 powerbi 目录下的 pbix 文件查看可视化报表

## 项目成果
1. 建成准实时因子计算框架，支撑6大维度百余项因子批量计算，个股综合评分响应秒级
2. 回测引擎经全历史数据与蒙特卡洛模拟验证，策略夏普比率达2.33
3. 形成可复用的量化数据处理范式，支撑多类策略快速迭代
