# Predicción de precios de casas

El presente proyecto se enfoca en la predicción de precios de casas, utilizando un conjunto de datos generado de manera aleatoria. Los datos fueron creados teniendo en cuenta los metros cuadrados habitables de las propiedades, lo cual establece una relación inicial entre el área y el precio. Este modelo sirve como un primer paso para comprender cómo se puede predecir el precio de una propiedad basándose en su tamaño, pero se espera expandir y mejorar este enfoque al incorporar más variables que puedan influir en el valor de mercado de una casa.

Como parte de la extensión del proyecto, se incorporará un conjunto de datos real disponible en Kaggle: USA Real Estate Dataset. Este dataset proporciona información adicional que permitirá un análisis más robusto de las propiedades, incluyendo características como ubicación, número de habitaciones, edad de la propiedad, características del vecindario, entre otras. Al incluir estos factores, se podrá realizar un análisis más profundo sobre cómo las diferentes variables impactan en el comportamiento de los precios de las viviendas.

## Generación del Modelo de Predicción

Para la construcción del modelo, se divide el conjunto de datos en dos partes: el 80% de los datos se utiliza para el entrenamiento del modelo, mientras que el 20% restante se destina a la evaluación de las predicciones. Este proceso asegura que el modelo se ajuste correctamente a los datos de entrenamiento y pueda generalizarse para hacer predicciones precisas sobre datos no vistos.

El conjunto de datos utilizado consta de 100 observaciones, lo que permite entrenar y probar el modelo con un número adecuado de ejemplos. El modelo de predicción implementado es una Regresión Lineal, una técnica estadística que busca establecer una relación lineal entre una variable dependiente (en este caso, el precio de la casa) y una o más variables independientes (en este caso, los metros cuadrados habitables de la casa).

Para la implementación del modelo, se utiliza Python junto con la biblioteca scikit-learn, que ofrece herramientas eficientes para construir y evaluar modelos de Machine Learning. A través de la regresión lineal, el modelo intenta encontrar la mejor línea recta que se ajuste a los datos, minimizando el error entre los valores predichos y los valores reales de los precios.

## CI/CD con Google Cloud Run

CI/CD (Integración Continua / Entrega Continua) es un conjunto de prácticas de desarrollo de software que permite automatizar la construcción, prueba y despliegue de aplicaciones. Estas prácticas tienen como objetivo mejorar la calidad del código, acelerar el ciclo de vida del desarrollo y garantizar que las aplicaciones sean siempre entregadas en condiciones óptimas.

Integración Continua (CI): Se refiere a la práctica de integrar cambios en el código con frecuencia, típicamente varias veces al día. Cada vez que un desarrollador realiza un cambio, se construye y prueba el código automáticamente para verificar que los nuevos cambios no rompen la funcionalidad existente.

Entrega Continua (CD): Implica la automatización de la entrega del código al entorno de producción o preproducción de forma continua, garantizando que el código esté siempre listo para ser desplegado, minimizando la intervención manual y acelerando el ciclo de desarrollo.

Pipeline de CI/CD con GitHub Actions y Google Cloud Run
Este proyecto está configurado para implementarse automáticamente en Google Cloud Run utilizando GitHub Actions. A continuación, se detallan los pasos clave de este pipeline de CI/CD:

1. Clonación del repositorio
Descripción: El primer paso en el pipeline de CI/CD es clonar el código fuente desde el repositorio de GitHub. Esto permite que las acciones automatizadas trabajen directamente con la última versión del código que se ha subido.
¿Por qué es importante?: Mantener el código actualizado es crucial para que las pruebas y despliegues se realicen sobre la versión más reciente del proyecto.
2. Autenticación con Google Cloud
Descripción: El pipeline necesita acceso a los recursos de Google Cloud para construir y desplegar la aplicación. Esto se logra mediante autenticación con Google Cloud usando credenciales específicas que permiten que GitHub Actions tenga permisos para interactuar con Google Cloud (como el Artifact Registry y Cloud Run).
¿Por qué es importante?: La autenticación asegura que solo las entidades autorizadas puedan realizar cambios en la infraestructura de Google Cloud, protegiendo el entorno de producción.
3. Construcción de la imagen Docker
Descripción: Una vez que el código está disponible y autenticado, se construye una imagen Docker del proyecto. Esta imagen contiene todo el entorno necesario para ejecutar la aplicación, incluidos el código fuente, dependencias y configuraciones.
¿Por qué es importante?: Las imágenes Docker aseguran que la aplicación se ejecute de manera consistente en cualquier entorno, desde el desarrollo hasta la producción.
4. Push a Google Artifact Registry
Descripción: Después de construir la imagen Docker, esta se sube (push) al Google Artifact Registry, un servicio gestionado de Google Cloud que almacena las imágenes Docker de manera segura y accesible para ser utilizadas en entornos de despliegue como Cloud Run.
¿Por qué es importante?: El Artifact Registry ofrece una ubicación centralizada y segura para almacenar las imágenes Docker, asegurando que solo las versiones verificadas se desplieguen en producción.
5. Despliegue en Cloud Run
Descripción: Finalmente, una vez que la imagen Docker está almacenada en Google Artifact Registry, el pipeline despliega la aplicación automáticamente en Google Cloud Run. Cloud Run es un servicio totalmente gestionado que ejecuta aplicaciones contenerizadas en un entorno escalable y sin servidor.
¿Por qué es importante?: Cloud Run simplifica el despliegue y la administración de aplicaciones contenerizadas, permitiendo escalar automáticamente en función de la demanda y proporcionando una solución eficiente y rentable para el despliegue de microservicios.
Resumen de los beneficios del pipeline CI/CD con Google Cloud Run:
Automatización: Todo el proceso, desde la construcción hasta el despliegue, se realiza de manera automática, reduciendo la intervención manual y aumentando la eficiencia.
Calidad: Las pruebas y validaciones automáticas aseguran que el código esté libre de errores antes de llegar a producción.
Escalabilidad: Con Google Cloud Run, la aplicación puede escalar automáticamente en función de la carga, asegurando que el rendimiento sea siempre óptimo.
Seguridad: El uso de autenticación y control de versiones garantiza que solo las versiones aprobadas y seguras sean desplegadas.
Este pipeline CI/CD con Google Cloud Run y GitHub Actions facilita un flujo de trabajo ágil, rápido y seguro para desarrollar y desplegar aplicaciones de manera eficiente. ¿Te gustaría añadir o ajustar algo más en este contexto?
