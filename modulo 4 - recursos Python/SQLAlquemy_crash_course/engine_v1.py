from sqlalchemy import create_engine, text

engine_lite = create_engine('sqlite:///database.db', echo=True)


con = engine_lite.connect()

print(engine_lite.pool.status())


with engine_lite.connect() as con: 
    
    with con.begin(): # bets -> context manegers dentro de ctxt managers realizando operações que precisam ser feitas em determinada ordem 
        sql = text('faz a operação #1') 
        
        resut = con.execute(sql) # isso é uma tupla
    
    with con.begin():
        sql2 = text('faz a operação #2') 
        
        resut = con.execute(sql2) 
    
    with con.begin():
    
        sql3 = text('faz a operação #3') 
        
        resut = con.execute(sql3) 

'''
    CONCEITOS ESSENCIAIS: 

    ENGINE: 
    
    CONNECTION POOL 
    
    DIALECT



'''