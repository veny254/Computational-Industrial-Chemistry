import pandas as pd
#defining data
data='advanced_messy_dataset.csv'
#loading data
df=pd.read_csv(data)
#inspectin the data
print(df.dtypes)
print(df.isna().sum())
#cleaning the data
clean_data=(df
.assign(annual_salary=lambda x 
:pd.to_numeric(x['annual_salary'],errors='coerce')
.where(lambda s:s>0).fillna(lambda s: s.median())
,age=lambda x:pd.to_numeric(x['age'],errors='coerce').fillna(lambda s: s.median())
,join_date=lambda x:pd.to_datetime(x['join_date'],errors='coerce').fillna(lambda s: s.mode()[0])
,q1_sales=lambda x: pd.to_numeric(x['q1_sales'],errors='coerce').fillna(lambda s: s.median())
,q2_sales=lambda x:pd.to_numeric(x['q2_sales'],errors='coerce').fillna(lambda s: s.median())))
print(clean_data['q1_sales'].isna().sum())
print(clean_data['q2_sales'].isna().sum())
print(clean_data.isna().sum())
#saving the clean data
clean_data.to_csv('advanced_Clean_dataset.csv')