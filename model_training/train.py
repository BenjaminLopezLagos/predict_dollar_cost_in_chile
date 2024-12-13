import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

base_train_dir = './model_training'

# Cargar datos
data = pd.read_csv(f'{base_train_dir}/data_extraction/processed_data.csv')
X = data[['year', 'month', 'day']]
y = data['usd_to_clp']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, f'{base_train_dir}/model.joblib')