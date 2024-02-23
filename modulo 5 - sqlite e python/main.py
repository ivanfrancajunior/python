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

# boa pratica [evitando esq injection]
sql_comand = (f'INSERT INTO {TABLA_NAME}'
'(name,weight) VALUES (:nome,:peso)')

# cursor.execute(sql_comand,[None,'Jota Apenas',9])

#listas
# cursor.executemany(sql_comand,[[None,'Bebel',7],[None,'Gustin',19],[None,'Lineuzinho',99] ])


#dicionarios 
cursor.executemany(sql_comand,[
    {'nome':'Bebel','peso':7},
    {'nome':'Gustin','peso':6},
    {'nome':'Lineuzinho','peso':71},
    
    ])





connection.commit()

cursor.close()
connection.close()