# Pipeline de Ingesta y Limpieza de Datos

## Descripción del proyecto

Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) utilizando Python y Pandas para procesar un dataset de compras de clientes de comercio electrónico.

El objetivo es automatizar la lectura, limpieza y almacenamiento de datos, aplicando buenas prácticas de modularización y optimización de memoria.

## Tecnologías utilizadas

- **Python 3:** lenguaje de programación.
- **Pandas:** lectura y transformación de datos.
- **PyArrow:** escritura y lectura de archivos Parquet.

## Estructura del proyecto

```text
Pipeline_Ingesta_Limpieza/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   └── transform.py
│
├── data/
│   └── customer_shopping_data.csv
│
└── output/
    └── customer_shopping_clean.parquet
```

**Nota:** Los archivos originales y procesados se almacenan localmente y no se incluyen en el repositorio. Esto evita subir archivos de datos que pueden generarse nuevamente al ejecutar el pipeline.

## Etapas del pipeline

### 1. Extracción

El módulo `extract.py` utiliza Pandas para leer el archivo CSV. Se aplican técnicas de optimización de tipos de datos, como `downcast` para variables numéricas y `category` para variables categóricas con pocos valores únicos.

### 2. Transformación

El módulo `transform.py` realiza las siguientes tareas:

- Normalización de nombres de columnas a minúsculas y formato snake_case.
- Eliminación de registros duplicados.
- Tratamiento de valores nulos mediante la mediana para variables numéricas y la categoría `Unknown` para variables categóricas.

### 3. Carga

El archivo `main.py` coordina las etapas y exporta los datos procesados a formato Parquet mediante Pandas y PyArrow.

Se elige Parquet por ser un formato columnar, comprimido y eficiente para el almacenamiento y procesamiento de datos, especialmente en flujos de trabajo de Machine Learning.

## Instalación y ejecución

### Requisitos previos

Tener Python 3 instalado.

### 1. Clonar el repositorio

Reemplazar `TU_USUARIO` por el nombre de usuario de GitHub:

```bash
git clone https://github.com/TU_USUARIO/Pipeline_Ingesta_Limpieza.git
cd Pipeline_Ingesta_Limpieza
```

### 2. Crear un entorno virtual

```powershell
py -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5. Ejecutar el pipeline

```powershell
python main.py
```

El archivo CSV debe estar ubicado en la carpeta `data/`, con el nombre `customer_shopping_data.csv`.

Al ejecutar el programa, se generará automáticamente la carpeta `output/` con el archivo procesado `customer_shopping_clean.parquet`.

## Resultados de la ejecución

Durante las pruebas realizadas se obtuvieron los siguientes resultados:

- Registros procesados: **3.900**
- Registros duplicados eliminados: **0**
- Valores nulos restantes: **0**
- Archivo de salida generado correctamente en formato Parquet.

## Conclusión

El proyecto permite automatizar un proceso de ingesta y limpieza de datos mediante una estructura modular y reutilizable. La separación entre extracción, transformación y carga facilita el mantenimiento y la ampliación del pipeline para futuros procesos de análisis de datos y Machine Learning.
