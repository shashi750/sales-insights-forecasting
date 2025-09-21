import pandas as pd

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\retail_sales_cleaned.csv")

# 🔹 Total retail + warehouse sales
total_retail = df["RETAIL SALES"].sum()
total_warehouse = df["WAREHOUSE SALES"].sum()
print("✅ Total Retail Sales:", round(total_retail, 2))
print("✅ Total Warehouse Sales:", round(total_warehouse, 2))

# 🔹 Top 5 suppliers by total sales (retail + warehouse)
df["TOTAL SALES"] = df["RETAIL SALES"] + df["WAREHOUSE SALES"]
top_suppliers = df.groupby("SUPPLIER")["TOTAL SALES"].sum().sort_values(ascending=False).head(5)
print("\n🔹 Top 5 Suppliers by Sales:")
print(top_suppliers)

# 🔹 Monthly sales trend (sum of sales grouped by year+month)
df["DATE"] = pd.to_datetime(df["YEAR"].astype(str) + "-" + df["MONTH"].astype(str) + "-01")
monthly_sales = df.groupby("DATE")["TOTAL SALES"].sum()
print("\n🔹 Monthly Sales Trend:")
print(monthly_sales.head(10))  # show first 10 months
