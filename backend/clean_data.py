import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\Retail_sales.csv")

# Remove rows with negative values in sales columns
df = df[(df['RETAIL SALES'] >= 0) & (df['RETAIL TRANSFERS'] >= 0) & (df['WAREHOUSE SALES'] >= 0)]

# Fill missing supplier names with "Unknown"
df['SUPPLIER'] = df['SUPPLIER'].fillna("Unknown")

# Save cleaned dataset
output_path = r"C:\Users\TiaaUser\Documents\Future career_ai\sales-insights-forecasting\data_sample\retail_sales_cleaned.csv"
df.to_csv(output_path, index=False)

print("✅ Cleaned dataset saved at:", output_path)
print("Rows before cleaning:", 30000)
print("Rows after cleaning:", len(df))
