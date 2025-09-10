# ETLProject/Load/ETLload.py
from sqlalchemy import create_engine
from Config.ETLconfig import DATABASE_URL

class Loader:
    """
    Clase para cargar los datos limpios a un destino.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path):
        """
        Guarda el DataFrame limpio en un archivo CSV.
        """
        try:
            self.df.to_csv(output_path, index=False)
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_mysql(self, table_name):
        """
        Guarda el DataFrame limpio en una base de datos MySQL.
        """
        try:
            # Crear la conexión con la base de datos MySQL utilizando SQLAlchemy
            engine = create_engine(DATABASE_URL)
            # Guardar el DataFrame en la tabla de MySQL
            self.df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            print(f"Datos guardados en la base de datos MySQL, tabla: {table_name}")
        except Exception as e:
            print(f"Error al guardar en MySQL: {e}")
