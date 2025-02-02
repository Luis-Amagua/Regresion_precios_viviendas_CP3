# Predicción de precios de casas

El presente proyecto se enfoca en la predicción de precios de casas, utilizando un conjunto de datos generado de manera aleatoria. Los datos fueron creados teniendo en cuenta los metros cuadrados habitables de las propiedades, lo cual establece una relación inicial entre el área y el precio. Este modelo sirve como un primer paso para comprender cómo se puede predecir el precio de una propiedad basándose en su tamaño

Como parte de la extensión del proyecto, se incorporará un conjunto de datos real disponible en Kaggle: https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset, este dataset proporciona información adicional que permitirá un análisis más robusto de las propiedades, incluyendo características como ubicación, número de habitaciones, edad de la propiedad, características del vecindario, entre otras. Al incluir estos factores, se podrá realizar un análisis más profundo sobre cómo las diferentes variables impactan en el comportamiento de los precios de las viviendas.

## Generación del Modelo de Predicción

El modelo se construye dividiendo los datos en un 80% para entrenamiento y un 20% para evaluación. Con un conjunto de 100 observaciones, se utiliza una Regresión Lineal para predecir el precio de las casas basado en los metros cuadrados habitables. La implementación se realiza en Python utilizando la biblioteca scikit-learn, que ayuda a ajustar la mejor línea recta entre los datos, minimizando el error entre las predicciones y los valores reales.

## CI/CD con Google Cloud Run

CI/CD (Integración Continua / Entrega Continua) automatiza la construcción, prueba y despliegue de aplicaciones para mejorar la calidad del código y acelerar el ciclo de desarrollo. Integración Continua (CI) se enfoca en integrar cambios frecuentemente y asegurar que el código no rompa funcionalidades. Entrega Continua (CD) automatiza el despliegue continuo en producción o preproducción.

Pipeline de CI/CD con GitHub Actions y Google Cloud Run:

Clonación del repositorio: Se clona el código desde GitHub para trabajar con la última versión.
Autenticación con Google Cloud: Se autentica el pipeline para acceder a los recursos de Google Cloud.
Construcción de la imagen Docker: Se crea una imagen Docker del proyecto, garantizando consistencia entre entornos.
Push a Google Artifact Registry: La imagen Docker se sube al Artifact Registry para su almacenamiento seguro.
Despliegue en Cloud Run: Finalmente, la imagen se despliega en Google Cloud Run, un servicio escalable y sin servidor.
Este pipeline automatiza el flujo de trabajo, asegurando despliegues rápidos y consistentes.
Resumen de los beneficios del pipeline CI/CD con Google Cloud Run:
Automatización: Todo el proceso, desde la construcción hasta el despliegue, se realiza de manera automática, reduciendo la intervención manual y aumentando la eficiencia.
Calidad: Las pruebas y validaciones automáticas aseguran que el código esté libre de errores antes de llegar a producción.
Escalabilidad: Con Google Cloud Run, la aplicación puede escalar automáticamente en función de la carga, asegurando que el rendimiento sea siempre óptimo.
Seguridad: El uso de autenticación y control de versiones garantiza que solo las versiones aprobadas y seguras sean desplegadas.
Este pipeline CI/CD con Google Cloud Run y GitHub Actions facilita un flujo de trabajo ágil, rápido y seguro para desarrollar y desplegar aplicaciones de manera eficiente. ¿Te gustaría añadir o ajustar algo más en este contexto?
