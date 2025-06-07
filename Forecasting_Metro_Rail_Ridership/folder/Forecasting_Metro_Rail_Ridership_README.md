
# Forecasting Metro Rail Ridership

## 📌 Objective
This project focuses on forecasting hourly metro rail ridership using raw entry-level data from February 2023. The aim is to help urban planners and transport authorities predict passenger flow patterns, enabling smarter operational decisions like train frequency adjustments, scheduling, and crowd control.

## 📂 Repository Contents

| File Name                          | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `Forecasting_Metro_Rail_Ridership.ipynb` | Fully documented notebook performing data aggregation, EDA, feature engineering, and forecasting using multiple time series models. |
| `02_2023.csv`                     | Raw hourly station-wise metro ridership data for February 2023.            |

## 🧾 Dataset Details

The dataset `02_2023.csv` contains over 200,000 records for the entire month of February 2023. Each row represents the number of passengers who entered a metro station during a specific hour.

| Column Name           | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `Entry Date`          | Date in the format `dd-mm-yyyy`                           |
| `Entry Hour`          | Hour of entry (0–23)                                      |
| `entry_lineid_sttnid` | Line and station identifier                               |
| `Entry TCK_MAIN_TP`   | Ticket type                                               |
| `Entry Count`         | Number of entries at that time, station, and ticket type |
| `Entry Station Code`  | Unique code for each metro station                        |
| `Month-Year`          | Used for filtering; dropped in later steps                |

## 🔍 Methodology

### 1. Data Preprocessing
- Parsed `Entry Date` and `Entry Hour` into a proper datetime object (`Datetime`)
- Aggregated station-wise entry counts into hourly totals
- Created features such as `Hour` and `is_rush_hour` for temporal insights

### 2. Exploratory Data Analysis (EDA)
- Identified ridership peaks (morning and evening rush hours)
- Analyzed station-wise and hourly patterns
- Visualized anomalies and holidays (e.g., Holi festival)

### 3. Feature Engineering
- `is_rush_hour`: Flagged hours 8–10 AM and 5–8 PM
- `is_holiday`: Manually marked known public holidays (e.g., Holi on March 8)
- Time-based features used to train machine learning models

### 4. Forecasting Models

| Model     | Library Used      | Purpose                          |
|-----------|-------------------|----------------------------------|
| ARIMA     | `pmdarima`        | Baseline statistical model       |
| SARIMA    | `statsmodels`     | Captures seasonal patterns       |
| Prophet   | `fbprophet`       | Robust forecasting with holidays |
| XGBoost   | `xgboost`         | Supervised regression with lags  |
| LSTM      | `tensorflow.keras`| Deep learning on time series     |

## 📊 Evaluation Metrics

| Model     | MAE (Feb) | RMSE (Feb) | Observations                              |
|-----------|-----------|------------|-------------------------------------------|
| Prophet   | ~20,702   | ~21,318    | Best performer across metrics             |
| XGBoost   | ~30,433   | ~50,185    | Interpretable; strong second choice       |
| ARIMA     | ~53,352   | ~69,578    | Baseline model; improved after tuning     |
| LSTM      | -         | -          | Overfit due to limited time span          |
| SARIMA    | -         | -          | Seasonal pattern visible, but less stable |

## 📈 Key Visualizations (Inside Notebook)
- Hourly ridership trends
- Entry count distribution by station
- Actual vs. predicted curves
- Holiday dips and peak hour spikes
- Model comparison graphs

## 🧠 Insights & Recommendations
- Commuter traffic is highest during 8–10 AM and 6–8 PM.
- Ridership drops on holidays and late-night hours.
- Prophet is the most robust choice for short-term forecasts.
- For future improvements, adding multiple months of data or real-time weather can enhance LSTM or hybrid models.

## ▶️ How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/your_repo_name.git
   ```

2. Open `Forecasting_Metro_Rail_Ridership.ipynb` in Jupyter Notebook or Google Colab.

3. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn prophet xgboost scikit-learn pmdarima statsmodels
   ```

4. Run all cells sequentially to reproduce results and forecasts.

## 🔒 License & Credits
This project was completed as part of an academic machine learning internship and uses public domain data. All preprocessing, modeling, and visualization scripts are original and documented for academic and future use.
