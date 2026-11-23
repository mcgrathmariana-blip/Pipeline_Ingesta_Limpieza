# Pipeline de Ingesta y Limpieza de Datos

## Descripción del proyecto

Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) utilizando Python y Pandas para procesar un dataset de compras de clientes de comercio electrónico.

El objetivo es automatizar la lectura, limpieza y almacenamiento de datos, aplicando buenas prácticas de modularización y optimización de memoria.

## Tecnologías utilizadas

- Python 3
- Pandas: lectura y transformación de datos.
- PyArrow: escritura y lectura de archivos Parquet.

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

Nota: los archivos originales y procesados se almacenan localmente y no se incluyen en el repositorio.

## Etapas del pipeline

### 1. Extracción

El módulo `extract.py` utiliza Pandas para leer el archivo CSV. Se aplican técnicas de optimización de tipos de datos, como `downcast` para variables numéricas y `category` para variables categóricas con pocos valores únicos.

### 2. Transformación

El módulo `transform.py` realiza las siguientes tareas:

- Normalización de nombres de columnas a minúsculas y formato snake_case.
- Eliminación de registros duplicados.
- Tratamiento de valores nulos mediante la mediana para variables numéricas y la categoría "Unknown" para variables categóricas.

### 3. Carga

El archivo `main.py` coordina las etapas y exporta los datos procesados a formato Parquet mediante Pandas y PyArrow.

Se elige Parquet por ser un formato columnar, comprimido y eficiente para el almacenamiento y procesamiento de datos, especialmente en flujos de trabajo de Machine Learning.

## Instalación y ejecución

### Requisitos previos

Tener Python 3 instalado.

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd Pipeline_Ingesta_Limpieza
```

### 2. Crear un entorno virtual

```bash
py -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv