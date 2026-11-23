
import pandas as pd


def extract_data(file_path):
    """
    Lee un archivo CSV y optimiza los tipos de datos.
    """

    # Leer el archivo
    df = pd.read_csv(file_path, low_memory=False)

    # Optimizar columnas numéricas
    for column in df.select_dtypes(include=["integer"]).columns:
        df[column] = pd.to_numeric(df[column], downcast="integer")

    for column in df.select_dtypes(include=["float"]).columns:
        df[column] = pd.to_numeric(df[column], downcast="float")

    # Convertir columnas de texto con pocos valores únicos
    # a tipo category para ahorrar memoria
    for column in df.select_dtypes(include=["object"]).columns:
        if df[column].nunique() / max(len(df), 1) < 0.5:
            df[column] = df[column].astype("category")

    print("Extracción completada correctamente.")
    print(f"Registros obtenidos: {len(df)}")
    print(f"Columnas obtenidas: {len(df.columns)}")
    print(f"Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

    return df
