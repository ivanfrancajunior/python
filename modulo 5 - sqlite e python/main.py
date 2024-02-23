# DOC: https://www.sqlite.org/doclist.html

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'mydb.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)


# criando tabela 
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# boa pratica [evitando esq injection]
sql_comand = (f'INSERT INTO {TABLE_NAME}'
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

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = 1'
)
connection.commit()

cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=67.89 '
        'WHERE id = 5'
    )
connection.commit()

cursor.close()
connection.close()



