# Computational Industrial Chemistry

A repository for data cleaning and analysis scripts related to computational industrial chemistry.

## Files

### Data_cleaning_6.py
A Python script for cleaning and preparing messy datasets for analysis.

**Features:**
- Loads data from CSV files
- Handles missing values intelligently
- Cleans numerical columns (salary, age, sales data)
- Converts date columns to proper datetime format
- Removes invalid data (negative salaries)
- Fills missing values with median (for numerical data) or mode (for dates)
- Exports cleaned data to a new CSV file

**Input:** `advanced_messy_dataset.csv`

**Output:** `advanced_Clean_dataset.csv`

**Cleaned Columns:**
- `annual_salary`: Converted to numeric, negatives removed, missing values filled with median
- `age`: Converted to numeric, missing values filled with median
- `join_date`: Converted to datetime, missing values filled with mode
- `q1_sales`: Converted to numeric, missing values filled with median
- `q2_sales`: Converted to numeric, missing values filled with median

**Usage:**
```bash
python Data_cleaning_6.py
```

## Requirements
- pandas
- os (standard library)

## Notes
- The script expects `advanced_messy_dataset.csv` to exist in the same directory
- Data cleaning strategy prioritizes preserving data integrity while handling missing values
- Cleaned dataset is saved with the same structure as the original
