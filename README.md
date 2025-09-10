# Prueba_BIGDATA_ELT

Proyecto ETL (Extract, Transform, Load) para procesar datos de restaurantes. Este flujo permite extraer información desde un CSV, limpiar y transformar los datos, y cargarlos en una base de datos MySQL.

Estructura del proyecto
Prueba_BIGDATA_ELT/
├── Config/
│   └── ETLconfig.py           # Configuración del proyecto y conexión a DB
├── Extract/
│   └── ETLextract.py          # Código para extraer los datos desde CSV
├── Transform/
│   └── ETLtransform.py        # Código para limpiar y transformar los datos
├── Load/
│   └── ETLload.py             # Código para cargar los datos en CSV o MySQL
├── Data/
│   └── Datos_Restaurant.csv   # Archivo CSV original
├── Main.py                    # Script principal para ejecutar el flujo ETL
├── requirements.txt           # Dependencias necesarias del proyecto
├── .env                       # Variables de entorno (DB, rutas de archivos)
└── README.md                  # Este archivo

Instalación y configuración

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd Prueba_BIGDATA_ELT


Crear un entorno virtual:

Linux / Mac:

python3 -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Configurar las variables de entorno:

Crea un archivo .env con el siguiente contenido:

DBUSER=root
DBPASSWORD=tu_contraseña
DBHOST=host_de_tu_db
DBPORT=puerto_db
DBNAME=nombre_db

CSV_PATH=./Data/Datos_Restaurant.csv
OUTPUT_PATH=./Data/Datos_Restaurant_Limpio.csv
DATABASE_URL=mysql+pymysql://${DBUSER}:${DBPASSWORD}@${DBHOST}:${DBPORT}/${DBNAME}

Uso

Ejecutar el flujo ETL completo:

python Main.py


Flujo que realiza:

Extract: Carga los datos desde CSV_PATH.

Transform: Limpia y transforma los datos:

Convierte fechas correctamente.

Rellena valores numéricos nulos con 0.

Rellena valores de texto nulos con "Unknown".

Corrige problemas de comillas dobles.

Load: Guarda los datos limpios en:

CSV de salida (OUTPUT_PATH).

Base de datos MySQL (DATABASE_URL).

Verificar resultados:

El CSV limpio se genera en:

./Data/Datos_Restaurant_Limpio.csv


Los datos se cargan en la tabla restaurantes de tu base de datos MySQL.

Dependencias

Python 3.12+

pandas

sqlalchemy

pymysql

python-dotenv

Notas

Asegúrate de que el archivo CSV original exista en la ruta definida en .env.

No incluyas datos sensibles como usuario o contraseña en tu repositorio público.

Se recomienda usar un entorno virtual para aislar dependencias.