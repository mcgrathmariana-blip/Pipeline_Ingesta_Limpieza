
from pathlib import Path

from src.extract import extract_data
from src.transform import transform_data


# Directorio principal del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Rutas de entrada y salida
INPUT_FILE = BASE_DIR / "data" / "customer_shopping_data.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "customer_shopping_clean.parquet"


def main():

    # 1. Extracción
    print("\n--- ETAPA 1: EXTRACCIÓN ---")
    df = extract_data(INPUT_FILE)

    # 2. Transformación
    print("\n--- ETAPA 2: TRANSFORMACIÓN ---")
    df_clean = transform_data(df)

    # 3. Carga en formato Parquet
    print("\n--- ETAPA 3: CARGA ---")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df_clean.to_parquet(
        OUTPUT_FILE,
        engine="pyarrow",
        index=False
    )

    print("\nPipeline ejecutado correctamente.")
    print(f"Archivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
