import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Definir los rangos para el área y el precio
area_min, area_max = 30, 130
precio_min, precio_max = 60000, 400000

# Generar áreas aleatorias entre 30 y 130 m²
areas = np.random.randint(area_min, area_max+1, size=100)

# Relación base para el precio en función del área (podemos hacer una fórmula más compleja)
# Por ejemplo, asumimos que el precio depende linealmente del área, pero con variabilidad
precios_base = areas * np.random.uniform(1000, 4000)  # Factor aleatorio para la relación área-precio

# Agregar ruido aleatorio al precio para aumentar la variabilidad
ruido = np.random.randint(-20000, 20000, size=100)  # Ruido aleatorio para aumentar la variabilidad

# Generar los precios finales
precios = precios_base + ruido

# Asegurarnos de que los precios estén dentro del rango adecuado (ajustar si es necesario)
precios = np.clip(precios, precio_min, precio_max)

# Crear el DataFrame
data = pd.DataFrame({
    'Área': areas,
    'Precio': precios
})
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
