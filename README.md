# Predicción de precios de casas

El presente proyecto se enfoca en la predicción de precios de casas, utilizando un conjunto de datos generado de manera aleatoria. Los datos fueron creados teniendo en cuenta los metros cuadrados habitables de las propiedades, lo cual establece una relación inicial entre el área y el precio. Este modelo sirve como un primer paso para comprender cómo se puede predecir el precio de una propiedad basándose en su tamaño

Como parte de la extensión del proyecto, se incorporará un conjunto de datos real disponible en Kaggle: https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset, este dataset proporciona información adicional que permitirá un análisis más robusto de las propiedades, incluyendo características como ubicación, número de habitaciones, edad de la propiedad, características del vecindario, entre otras. Al incluir estos factores, se podrá realizar un análisis más profundo sobre cómo las diferentes variables impactan en el comportamiento de los precios de las viviendas.

## Generación del Modelo de Predicción

El modelo se construye dividiendo los datos en un 80% para entrenamiento y un 20% para evaluación. Con un conjunto de 100 observaciones, se utiliza una Regresión Lineal para predecir el precio de las casas basado en los metros cuadrados habitables. La implementación se realiza en Python utilizando la biblioteca scikit-learn, que ayuda a ajustar la mejor línea recta entre los datos, minimizando el error entre las predicciones y los valores reales.

![image](https://github.com/user-attachments/assets/a463e025-fe93-47e4-ab3f-3ac9712bc051)

## CI/CD con Google Cloud Run

CI/CD (Integración Continua / Entrega Continua) automatiza la construcción, prueba y despliegue de aplicaciones para mejorar la calidad del código y acelerar el ciclo de desarrollo. Integración Continua (CI) se enfoca en integrar cambios frecuentemente y asegurar que el código no rompa funcionalidades. Entrega Continua (CD) automatiza el despliegue continuo en producción o preproducción.

Pipeline de CI/CD con GitHub Actions y Google Cloud Run:

1. Clonación del repositorio: Se clona el código desde GitHub para trabajar con la última versión.
2. Autenticación con Google Cloud: Se autentica el pipeline para acceder a los recursos de Google Cloud.
3. Construcción de la imagen Docker: Se crea una imagen Docker del proyecto, garantizando consistencia entre entornos.
4. Push a Google Artifact Registry: La imagen Docker se sube al Artifact Registry para su almacenamiento seguro.
5. Despliegue en Cloud Run: Finalmente, la imagen se despliega en Google Cloud Run, un servicio escalable y sin servidor.
Este pipeline automatiza el flujo de trabajo, asegurando despliegues rápidos y consistentes.

