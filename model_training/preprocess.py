import pandas as pd
import os

print(os.getcwd())
base_data_dir = './model_training/data_extraction'

df = pd.read_excel(f'{base_data_dir}/data.xlsx', engine="openpyxl")
df = df.iloc[2::]
df.reset_index(drop=True)
og_columns = df.columns

df = df.rename(columns={og_columns[0]: 'periodo', og_columns[1]: 'pesos por dolar'})
df['pesos por dolar'] = pd.to_numeric(df['pesos por dolar'])
df['periodo'] = pd.to_datetime(df['periodo'])  # <-- omit if datetime_utc is already datetime64[ns]
df[['year', 'month', 'day']] = df['periodo'].apply(lambda x: x.timetuple()[:3]).tolist()
df = df.drop('periodo', axis=1)
column_to_move = df.pop('pesos por dolar')
df.insert(og_columns.size+1, 'usd_to_clp', column_to_move)

df.to_csv(f'{base_data_dir}/processed_data.csv', ',')
