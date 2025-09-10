# ETLProject/Main.py
from Extract.ETLextract import extract_data
from Transform.ETLtransform import transform_data
from Load.ETLload import load_data

def run_etl():
    """
    Ejecuta el flujo ETL completo.
    """
    # Extraer
    df = extract_data()
    if df is None:
        return
    
    # Transformar
    df_transformed = transform_data(df)
    if df_transformed is None:
        return
    
    # Cargar
    load_data(df_transformed)

if __name__ == "__main__":
    run_etl()
