
import pandas as pd

# Load dataset (case-sensitive file name)

df = pd.read_csv(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\Retail_sales.csv")


# Show first 5 rows
print("🔹 First 5 rows:")
print(df.head())

# Show column names
print("\n🔹 Columns in dataset:")
print(df.columns.tolist())

# Show summary statistics
print("\n🔹 Summary statistics:")
print(df.describe(include="all"))
