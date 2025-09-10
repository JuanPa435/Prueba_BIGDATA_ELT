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



        num_cols_coma = ['Precio unita COP', 'Costo Unit COP']
        for col in num_cols_coma:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('"', '', regex=False).str.replace(",", ".", regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce')

    
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.replace('"', '', regex=False).str.replace("'", '', regex=False).str.strip()

        print("Valores nulos antes de la transformación:")
        print(df.isnull().sum())

        # Limpieza de la columna 'Fecha'
        if 'Fecha' in df.columns:
            df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce', format='%d/%m/%Y')
            df['Fecha'] = df['Fecha'].fillna('Fecha Desconocida')
            # Formatear la fecha sin hora
            df['Fecha'] = df['Fecha'].apply(lambda x: x.strftime('%Y-%m-%d') if x != 'Fecha Desconocida' and pd.notnull(x) else x)


        # Rellenar valores nulos en columnas numéricas con 0
        num_cols = ['Precio unita COP', 'Costo Unit COP', 'quantity']
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        text_cols = ['item_name', 'transaction_type', 'received_by', 'time_of_sale']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown')  


        df['item_name'] = df['item_name'].fillna('Unknown')

        df = df.dropna(subset=['item_name', 'Precio unita COP'])  


        print("Valores nulos después de la transformación:")
        print(df.isnull().sum())


        df = df.where(pd.notnull(df), 'null')
        self.df = df
        return self.df
