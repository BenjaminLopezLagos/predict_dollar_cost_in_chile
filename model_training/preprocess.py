import pandas as pd
import os

print(os.getcwd())
base_data_dir = './model_training/data_extraction'

df = pd.read_csv(f'{base_data_dir}/scripts/data.csv')
df['pesos por dolar'] = pd.to_numeric(df['pesos por dolar'])
df['periodo'] = pd.to_datetime(df['periodo'])  # <-- omit if datetime_utc is already datetime64[ns]
df[['year', 'month', 'day']] = df['periodo'].apply(lambda x: x.timetuple()[:3]).tolist()
df = df.drop(['Unnamed: 0', 'periodo'], axis=1)
df.head()
column_to_move = df.pop('pesos por dolar')
df.insert(df.columns.size, 'usd_to_clp', column_to_move)

df.to_csv(f'{base_data_dir}/processed_data.csv', ',')
