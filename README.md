# README – Medical Insurance Cost Prediction (Flask + Machine Learning + Render)

Este proyecto implementa un modelo de Machine Learning para predecir el costo del seguro médico de una persona, utilizando datos demográficos y de estilo de vida.
La aplicación web está desarrollada con Flask, entrenada con un modelo lineal, y desplegada en Render, permitiendo a cualquier usuario acceder mediante un navegador web.

Este proyecto demuestra un flujo completo de trabajo en ciencia de datos y despliegue web:

  - Selección y exploración del dataset
  - Entrenamiento del modelo
  - Construcción de la API e interfaz con Flask
  - Integración del modelo con la aplicación web
  - Despliegue en Render

## Dataset: Medical Insurance Cost

Fuente: https://www.kaggle.com/datasets/mirichoi0218/insurance

| Variable     | Tipo       | Descripción                          |
| ------------ | ---------- | ------------------------------------ |
| **age**      | Numérica   | Edad del paciente                    |
| **bmi**      | Numérica   | Índice de masa corporal              |
| **children** | Numérica   | Número de hijos                      |
| **sex**      | Categórica | Hombre / Mujer                       |
| **smoker**   | Categórica | Fumador / No fumador                 |
| **region**   | Categórica | Región geográfica                    |
| **charges**  | Numérica   | Costo del seguro (variable objetivo) |


## Entrenamiento del Modelo

El modelo fue entrenado utilizando:

  - LinearRegression de Scikit-Learn
  - Preprocesamiento con:
    - OneHotEncoder para variables categóricas
    - ColumnTransformer para combinar numéricas y categóricas
      
### Métricas obtenidas

Tras entrenarlo con un train_test_split del 80/20:

  - R²: (varía según ejecución, pero típicamente ~0.74–0.78)
  - MSE: error medio cuadrático entre predicciones y valores reales

## Interfaz de Usuario

  - Diseño simple y limpio en HTML
  - Estilos personalizados en static/styles.css
  - Navegación fluida entre formulario → resultado

## Aplicación Web

### Funcionalidad

El usuario ingresa:

- Edad
- BMI
- Número de hijos
- Sexo
- Fumador o no
- Región

Y la app devuelve:

### 👉  Costo estimado del seguro médico

## Despliegue en Render

### URL pública:
(agrega aquí tu enlace de Render)
➡️ (https://ml-web-app-using-flask-4383.onrender.com/)

## Conclusiones

- El hábito de fumar, el BMI y la edad son las variables más influyentes.
- Los modelos lineales permiten interpretabilidad y facilidad de despliegue.
- Flask es ligero y adecuado para APIs y formularios web simples.
- Render ofrece un entorno sencillo y rápido para publicar aplicaciones web.

## Contributors


This template was built as part of the [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) by 4Geeks Academy by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Learn more about [4Geeks Academy BootCamp programs](https://4geeksacademy.com/us/programs) here.

Other templates and resources like this can be found on the school's GitHub page.
