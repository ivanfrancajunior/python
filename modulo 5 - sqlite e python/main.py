# DOC: https://www.sqlite.org/doclist.html

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'mydb.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLA_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# criando tabela 

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLA_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# registrandfo valores [ PIOR FORMA POSSIVEL ] ❌

cursor.execute(f'INSERT INTO {TABLA_NAME}'
' (id,name,weight) VALUES (NULL,"Apenas Jota", 60)'
)
connection.commit()


cursor.close()
connection.close()