import pandas as pd
import numpy as np

def clean_assay_data(file_path: str) -> pd.DataFrame:
    """
    Cleans high-throughput laboratory assay records, standardizes schemas,
    imputes missing values, and removes statistical outliers via IQR method.
    """
    print(f"Ingesting assay records from {file_path}...")
    df = pd.read_csv(file_path)
    
    # Standardize column headers (snake_case conversion)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    initial_count = len(df)
    
    # Handle missing values in measurement metrics
    if 'absorbance' in df.columns:
        df['absorbance'] = df['absorbance'].fillna(df['absorbance'].median())
        
    # Isolate and filter out concentration outliers using IQR
    if 'concentration_um' in df.columns:
        q1 = df['concentration_um'].quantile(0.25)
        q3 = df['concentration_um'].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        df = df[(df['concentration_um'] >= lower_bound) & (df['concentration_um'] <= upper_bound)]
        
    print(f"Cleaning finished. Filtered {initial_count - len(df)} anomalous records. Retained {len(df)} clean rows.")
    return df

if __name__ == "__main__":
    # Example execution
    # cleaned_df = clean_assay_data("raw_assay_results.csv")
    # cleaned_df.to_csv("cleaned_assay_output.csv", index=False)
    pass