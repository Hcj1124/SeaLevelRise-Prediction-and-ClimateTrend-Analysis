# 氣候趨勢分析: 預測海平面上升狀況

本專案旨在透過資料分析與機器學習模型，探討全球氣候變遷（二氧化碳排放）與海平面上升之間的關聯性，並對未來十年的海平面變化進行預測。研究呼應聯合國永續發展目標 **SDG 13（氣候行動）** 與 **SDG 14（海洋生態系統）**。

## Project Overview
本研究整合了全球海平面資料集 (Global Sea Level)、大氣二氧化碳排放趨勢 (CO2 Emission) 以及北極海冰範圍 (Arctic Sea Ice Extent) 等數據，進行多維度的環境趨勢分析[cite: 6]。

## Tech Stack
* **語言**: Python
* **機器學習**: `scikit-learn` (Random Forest, Linear Regression)
* **數據處理**: `pandas`, `numpy`
* **視覺化**: `matplotlib`

## Key Analysis
本專案採用機器學習模型進行預測，並針對環境數據進行了標準化處理：
* **海平面上升預測**: 實作線性回歸模型，預測 2022-2031 年全球海平面變化趨勢[cite: 9]。
* **二氧化碳趨勢分析**: 建立 CO2 平均值模型，並分析其與海平面上升的潛在相關性[cite: 8]。
* **異常值處理**: 針對數據集中的離群值 (Outliers) 進行清洗，確保模型訓練的準確性與穩定性[cite: 6]。

## Key Findings
* **關聯性驗證**: 資料顯示二氧化碳排放增加導致全球氣溫升高，加速極地冰原融化，進而導致海平面上升[cite: 6]。

## Documentations
* `AP_Sea_Level.py`: 使用隨機森林模型評估海平面變化[cite: 7]。
* `Future_Sea_Level.py`: 線性回歸預測未來十年海平面上升趨勢[cite: 9]。
* `Future_CO2_Mean.py`: 預測未來二氧化碳濃度變化[cite: 8]。
* `25_海平面上升.pdf`: 完整專題報告[cite: 6]。
