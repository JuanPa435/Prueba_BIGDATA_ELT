# ETLProject/Main.py
import os
from Extract.ETLextract import extract_data
from Transform.ETLtransform import Transformer
from Load.ETLload import Loader
from Config.ETLconfig import OUTPUT_PATH

def run_etl():
    """
    Ejecuta el flujo ETL completo.
    """
    # Extraer
    df = extract_data()
    if df is None:
        return
    
    # Transformar
    transformer = Transformer(df)
    df_transformed = transformer.clean()
    if df_transformed is None:
        return
    
    # Cargar
    loader = Loader(df_transformed)
    loader.to_mysql('restaurantes')  # Cargar datos en la tabla 'restaurantes'
    
    # Guardar los datos transformados en un archivo CSV
    loader.to_csv(OUTPUT_PATH)  # Usar OUTPUT_PATH desde el archivo .env

if __name__ == "__main__":
    run_etl()
