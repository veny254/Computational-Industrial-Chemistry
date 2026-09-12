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

### Fitness center programm.py
An interactive Python program for managing fitness center membership eligibility and registration.

**Features:**
- Determines fitness program eligibility based on user age
- Validates medical condition information
- Guides users through membership plan selection
- Provides personalized pricing based on membership type and age

**Program Flow:**
1. **Age-Based Eligibility Check**
   - Age < 18 → Teens Fitness Program
   - Age 18-40 → Regular Fitness Program
   - Age > 40 → Senior Wellness Program

2. **Medical Condition Verification**
   - Validates user input (accepts "yes" or "no")
   - Users aged 40+ with medical conditions require Medical Clearance
   - Users without medical issues or under 40 can proceed with registration

3. **Membership Selection**
   - **Basic Plan:** $30/month (or $45/month with personal training)
   - **Premium Plan:** $60/month
   - Youth Discount: 10% off premium plans for members under 30

**Usage:**
```bash
python "Fitness center programm.py"
```

**Input:** Interactive prompts for age, medical condition, and membership preference

**Output:** Fitness program eligibility and membership pricing information

## Requirements
- pandas
- os (standard library)

## Notes
- The script expects `advanced_messy_dataset.csv` to exist in the same directory (for Data_cleaning_6.py)
- Data cleaning strategy prioritizes preserving data integrity while handling missing values
- Cleaned dataset is saved with the same structure as the original
