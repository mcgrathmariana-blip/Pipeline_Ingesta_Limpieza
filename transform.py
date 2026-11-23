
import pandas as pd


def transform_data(df):
    """
    Limpia y transforma el DataFrame:
    - Normaliza los nombres de las columnas.
    - Elimina registros duplicados.
    - Gestiona los valores nulos.
    """

    # 1. Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Eliminar registros duplicados
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)

    # 3. Gestionar valores nulos
    for column in df.columns:

        if df[column].isnull().sum() > 0:

            # Variables numéricas: reemplazar por la mediana
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())

            # Variables categóricas: reemplazar por Unknown
            else:
                df[column] = df[column].cat.add_categories(
                    ["Unknown"]
                ).fillna("Unknown") if isinstance(
                    df[column].dtype, pd.CategoricalDtype
                ) else df[column].fillna("Unknown")

    print("Transformación completada correctamente.")
    print(f"Duplicados eliminados: {duplicates_removed}")
    print(f"Valores nulos restantes: {df.isnull().sum().sum()}")
    print(f"Registros finales: {len(df)}")

    return df
