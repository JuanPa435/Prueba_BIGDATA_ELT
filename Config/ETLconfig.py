# ETLProject/Config/ETLconfig.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos
DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DBNAME = os.getenv("DBNAME")

# URL de conexión a la base de datos
DATABASE_URL = f"mysql+pymysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"

# Ruta del archivo CSV de entrada
CSV_PATH = os.getenv("CSV_PATH")

# Ruta del archivo CSV de salida (si es necesario)
OUTPUT_PATH = os.getenv("OUTPUT_PATH")
