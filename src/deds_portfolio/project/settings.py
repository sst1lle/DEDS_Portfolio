from pathlib import Path
from loguru import logger
import pandas 
import sqlite3
import warnings
warnings.simplefilter('ignore')

class Settings():

    conn = sqlite3.connect('sql/go_sales_train2.sqlite')
    print("SQLite3 Connection: ",conn)


    basedir= Path.cwd()
    rawdir = Path("data/raw")
    processeddir = Path("data/processed")
    logdir = basedir / "log"  

    tabellen = [
    "product", "product_type", "product_line", "sales_staff", 
    "sales_branch", "retailer_site", "country", "order_header", 
    "order_details", "returned_item", "return_reason"]


    dataframes = {}

    for tabel in tabellen:
        dataframes[tabel] = pandas.read_sql_query(f"SELECT * FROM {tabel}", conn)
        print(f"Tabel '{tabel}' ingelezen met {len(dataframes[tabel])} rijen.")

    conn.close()

 
settings = Settings()
logger.add("logfile.log")
