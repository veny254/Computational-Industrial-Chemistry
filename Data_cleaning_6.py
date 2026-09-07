import pandas as pd
import os

# Define data file path
data = 'advanced_messy_dataset.csv'

# Check if file exists
if not os.path.exists(data):
    raise FileNotFoundError(f"File {data} not found")

# Load data
df = pd.read_csv(data)

# Inspect the data
print("Data types:")
print(df.dtypes)
print("\nMissing values before cleaning:")
print(df.isna().sum())

# Clean the data
clean_data = df.copy()

# Clean annual_salary: convert to numeric, remove negatives, fill with median
clean_data['annual_salary'] = pd.to_numeric(clean_data['annual_salary'], errors='coerce')
clean_data.loc[clean_data['annual_salary'] <= 0, 'annual_salary'] = None
clean_data['annual_salary'].fillna(clean_data['annual_salary'].median(), inplace=True)

# Clean age: convert to numeric, fill with median
clean_data['age'] = pd.to_numeric(clean_data['age'], errors='coerce')
clean_data['age'].fillna(clean_data['age'].median(), inplace=True)

# Clean join_date: convert to datetime, fill with mode
clean_data['join_date'] = pd.to_datetime(clean_data['join_date'], errors='coerce')
mode_date = clean_data['join_date'].mode()
if len(mode_date) > 0:
    clean_data['join_date'].fillna(mode_date[0], inplace=True)

# Clean q1_sales: convert to numeric, fill with median
clean_data['q1_sales'] = pd.to_numeric(clean_data['q1_sales'], errors='coerce')
clean_data['q1_sales'].fillna(clean_data['q1_sales'].median(), inplace=True)

# Clean q2_sales: convert to numeric, fill with median
clean_data['q2_sales'] = pd.to_numeric(clean_data['q2_sales'], errors='coerce')
clean_data['q2_sales'].fillna(clean_data['q2_sales'].median(), inplace=True)

# Verify cleaning results
print("\nMissing values after cleaning:")
print(f"q1_sales NaN count: {clean_data['q1_sales'].isna().sum()}")
print(f"q2_sales NaN count: {clean_data['q2_sales'].isna().sum()}")
print("\nTotal missing values by column:")
print(clean_data.isna().sum())

# Save the clean data
clean_data.to_csv('advanced_Clean_dataset.csv', index=False)
print("\nCleaned data saved to 'advanced_Clean_dataset.csv'")
