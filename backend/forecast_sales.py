import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\retail_sales_cleaned.csv")

# Prepare data
df["DATE"] = pd.to_datetime(df["YEAR"].astype(str) + "-" + df["MONTH"].astype(str) + "-01")
df_grouped = df.groupby("DATE")[["RETAIL SALES", "WAREHOUSE SALES"]].sum().reset_index()
df_grouped["TOTAL SALES"] = df_grouped["RETAIL SALES"] + df_grouped["WAREHOUSE SALES"]

# Time series
ts = df_grouped.set_index("DATE")["TOTAL SALES"].asfreq("MS")  # Ensure monthly freq

# Fit ARIMA model
model = ARIMA(ts, order=(1,1,1))
fit = model.fit()

# Forecast next 6 months
forecast = fit.forecast(steps=6)

# Clip extreme outliers (prevent negative or unrealistic values)
forecast = forecast.clip(lower=0, upper=ts.max()*2)

# Save forecast
forecast_df = forecast.reset_index()
forecast_df.columns = ["DATE", "FORECASTED SALES"]
forecast_df.to_csv(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\sales_forecast.csv", index=False)

print("✅ Forecast saved to sales_forecast.csv")
print(forecast_df)

# Plot forecast vs historical
plt.figure(figsize=(10,5))
plt.plot(ts, label="Historical Sales", color="blue")
plt.plot(forecast_df["DATE"], forecast_df["FORECASTED SALES"], label="Forecast", color="red", marker="o")
plt.title("Sales Forecast (Next 6 Months)")
plt.legend()
plt.savefig(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\demo\forecast_plot.png")
plt.show()
