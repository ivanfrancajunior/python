'''
    CONCEITOS ESSENCIAIS: 

    ENGINE: 
        Ponto inicial para as aplicações que farão uso do SQLAlc, o mesmo fará todos
        os processos que vão interagir com a base de dados.
    
    CONNECTION POOL:
        O pool de conexões do SQLAlc é uma funcionalidade essencial para 
        gerenciar conexões de banco de dados de forma eficiente em aplicativos Python.

        Ele controla a quantidade de conexões abertas com o banco de dados, gerenciando-as conforme necessário para garantir um desempenho adequado 
        e evitar sobrecargas.  
    
    
    DIALECT: 
        O dialeto vai especificar com qual banco de dados o SQLAlc vai interagir.

'''

from sqlalchemy import create_engine,text

# inicia a engine e especifica o banco de dados
sqlite_engine = create_engine("sqlite:///database.db")

dialect = sqlite_engine.dialect

print(dialect) # <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x0000028523E090A0>

# inicianco a conexão e realizando primeira query

conn = sqlite_engine.connect()
query = text('SELECT * FROM filmes')
response = conn.execute(query)

for row in response: 
    print(row) # uma tupla com os dados da tabela
    print(row.titulo)

