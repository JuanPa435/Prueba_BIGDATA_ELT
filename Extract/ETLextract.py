# ETLProject/Extract/ETLextract.py
import pandas as pd
from Config.ETLconfig import CSV_PATH

def extract_data():
    """
    Extrae los datos desde un archivo CSV.
    """
    try:
        # Leer el archivo CSV con manejo adecuado de comillas y espacios
        df = pd.read_csv(CSV_PATH, quotechar='"', escapechar='\\', skipinitialspace=True, encoding='utf-8')

        # Limpiar espacios y comillas de los valores tipo texto
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip().str.replace('"', '', regex=False).str.replace("'", '', regex=False)

        print(f"Datos extraídos correctamente desde {CSV_PATH}")
        return df
    except Exception as e:
        print(f"Error al extraer los datos: {e}")
        return None
