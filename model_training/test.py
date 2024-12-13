import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import mean_squared_error, r2_score
import joblib

base_train_dir = './model_training'

# Cargar datos
data = pd.read_csv(f'{base_train_dir}/data_extraction/processed_data.csv')
X = data[['year', 'month', 'day']]
y = data['usd_to_clp']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cargar modelo
model = joblib.load(f'{base_train_dir}/model.joblib')

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular métricas
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.5f}")
print(f"R2 Score: {r2:.5f}")
