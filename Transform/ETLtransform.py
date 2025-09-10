# ETLProject/Transform/ETLtransform.py
import pandas as pd

class Transformer:
    """
    Clase para transformar y limpiar los datos extraídos.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        """
        Realiza limpieza y transformación de los datos.
        """
        df = self.df.copy()

        # Eliminar comillas dobles y simples de todas las columnas tipo texto
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.replace('"', '', regex=False).str.replace("'", '', regex=False)

        # Imprimir cantidad de valores nulos antes de la transformación
        print("Valores nulos antes de la transformación:")
        print(df.isnull().sum())

        # Limpieza de la columna 'Fecha'
        if 'Fecha' in df.columns:
            # Intentar convertir la columna 'Fecha' a datetime
            df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce', format='%d/%m/%Y')
            # Si la fecha no se pudo convertir (NaT), la reemplazamos con 'Fecha Desconocida'
            df['Fecha'] = df['Fecha'].fillna('Fecha Desconocida')

        # Rellenar valores nulos en columnas numéricas con 0
        num_cols = ['Precio unita COP', 'Costo Unit COP', 'quantity']
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)  # Reemplazar valores nulos con 0

        # Rellenar valores nulos en columnas de texto con 'Unknown'
        text_cols = ['item_name', 'transaction_type', 'received_by', 'time_of_sale']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown')  # Reemplazar valores nulos con 'Unknown'

        # Si 'item_name' es nulo, también rellenarlo con 'Unknown'
        df['item_name'] = df['item_name'].fillna('Unknown')

        # Verificar si las filas están completas antes de transformarlas
        df = df.dropna(subset=['item_name', 'Precio unita COP'])  # Eliminar filas donde 'item_name' o 'Precio unita COP' son nulos

        # Imprimir cantidad de valores nulos después de la transformación
        print("Valores nulos después de la transformación:")
        print(df.isnull().sum())

        self.df = df
        return self.df
