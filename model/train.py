import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generar dataset con areas entre 30 y 130 m2 y precio aprox
# Datos de ejemplo (Área en m² y Precio en dólares)
data = {
    'Área': [50, 80, 120, 150, 200, 250, 300, 350, 400],
    'Precio': [100000, 150000, 250000, 300000, 400000, 500000, 600000, 720000, 850000]
}
# Convertir a DataFrame
df = pd.DataFrame(data)

# Dividir los datos en conjuntos de entrenamiento y prueba
X = df[['Área']]
y = df['Precio']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse}")

# Visualización de los resultados
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Predicción del modelo')  # Línea de predicción sobre todos los puntos
plt.xlabel('Área')
plt.ylabel('Precio')
plt.title('RL Precio vs Área')
plt.legend()
plt.show()

# Guardar el modelo entrenado
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(modelo, f)

print("Modelo guardado en 'model.pkl'")
