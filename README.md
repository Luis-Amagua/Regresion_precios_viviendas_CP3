# Predicción de precios de casas

El presente proyecto se enfoca en la predicción de precios de casas, utilizando un conjunto de datos generado de manera aleatoria. Los datos fueron creados teniendo en cuenta los metros cuadrados habitables de las propiedades, lo cual establece una relación inicial entre el área y el precio. Este modelo sirve como un primer paso para comprender cómo se puede predecir el precio de una propiedad basándose en su tamaño, pero se espera expandir y mejorar este enfoque al incorporar más variables que puedan influir en el valor de mercado de una casa.

Como parte de la extensión del proyecto, se incorporará un conjunto de datos real disponible en Kaggle: USA Real Estate Dataset. Este dataset proporciona información adicional que permitirá un análisis más robusto de las propiedades, incluyendo características como ubicación, número de habitaciones, edad de la propiedad, características del vecindario, entre otras. Al incluir estos factores, se podrá realizar un análisis más profundo sobre cómo las diferentes variables impactan en el comportamiento de los precios de las viviendas.

## Generación del Modelo de Predicción

Para la construcción del modelo, se divide el conjunto de datos en dos partes: el 80% de los datos se utiliza para el entrenamiento del modelo, mientras que el 20% restante se destina a la evaluación de las predicciones. Este proceso asegura que el modelo se ajuste correctamente a los datos de entrenamiento y pueda generalizarse para hacer predicciones precisas sobre datos no vistos.

El conjunto de datos utilizado consta de 100 observaciones, lo que permite entrenar y probar el modelo con un número adecuado de ejemplos. El modelo de predicción implementado es una Regresión Lineal, una técnica estadística que busca establecer una relación lineal entre una variable dependiente (en este caso, el precio de la casa) y una o más variables independientes (en este caso, los metros cuadrados habitables de la casa).

Para la implementación del modelo, se utiliza Python junto con la biblioteca scikit-learn, que ofrece herramientas eficientes para construir y evaluar modelos de Machine Learning. A través de la regresión lineal, el modelo intenta encontrar la mejor línea recta que se ajuste a los datos, minimizando el error entre los valores predichos y los valores reales de los precios.
