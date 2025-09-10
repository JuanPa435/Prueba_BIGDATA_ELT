# ETLProject/Config/ETLconfig.py
import os
from dotenv import load_dotenv

load_dotenv()

DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"mysql+pymysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"

CSV_PATH = os.getenv("CSV_PATH")

OUTPUT_PATH = os.getenv("OUTPUT_PATH")
