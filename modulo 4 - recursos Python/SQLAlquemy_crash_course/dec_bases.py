'''
    MAPEAMENTO DECLARATIVO: 

    No SQLAlchemy, podemos usar o mapeamento declarativo para definir modelos de
    tabelas de banco de dados de uma maneira mais orientada a objetos. 
    
    Além disso, podemos usar bases declarativas para representar um conjunto de 
    classes mapeadas de forma declarativa. 


    # Classes Declarativas:

        Classes declarativas no SQLAlchemy são usadas para definir modelos 
        de dados que representam tabelas de banco de dados de uma forma mais 
        orientada a objetos. 
        Em vez de definir tabelas diretamente, você cria classes Python que 
        representam essas tabelas. Cada classe normalmente corresponde a uma 
        tabela no banco de dados e os atributos da classe     

        
        Cada classe normalmente corresponde a uma tabela no banco de dados e os atributos da classe correspondem às colunas da tabela. Isso permite que 
        você trabalhe com os dados do banco de dados usando objetos Python, o 
        que torna o código mais legível e mais fácil de entender.

    # Sessões:
        As sessões no SQLAlc são usadas para gerenciar transações e 
        interações com o banco de dados. 

        Elas representam uma conexão com o banco de dados e permitem que você 
        execute consultas, insira, atualize e exclua registros.

        As sessões mantêm um rastreamento das mudanças feitas nos objetos do 
        banco de dados durante uma transação e as refletem quando você confirma 
        a transação. 
        
        Isso garante consistência nos dados e oferece a capacidade de desfazer alterações se necessário(rollbacks).

        As sessões também fornecem recursos de cache para melhorar o desempenho, armazenando objetos consultados em memória para acesso rápido 
        posteriormente.    

'''

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# inicia a engine e especifica o banco de dados
sqlite_engine = create_engine("sqlite:///database.db")

conn = sqlite_engine.connect()

# Entidade Filme
#


# iniciada classe que reflete os filmes na db
class Base(DeclarativeBase):
    pass 


# ❌ class Filmes(DeclarativeBase): ->  Cannot use 'DeclarativeBase' directly as a declarative base class. Create a Base by creating a subclass of it.


class Filmes(Base): 
    __tablename__= 'filmes'
    
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f'Filme (titulo={self.titulo}, genero={self.genero}, ano={self.ano} )'

# inicia e binda  a sessão com a base de dados que realizara as interações
Session = sessionmaker(bind=sqlite_engine)
session = Session()

#Insert - C
data_to_insert = Filmes(titulo='Pelé', genero='Comédia', ano=2023)
session.add(data_to_insert)
session.commit()
session.close()

# Select - R
data = session.query(Filmes).all()

#Update - U
session.query(Filmes).filter(Filmes.ano == 23).update({"ano": 2023})
session.commit()
session.close()


# Delete -D
session.query(Filmes).filter(Filmes.titulo == 'algo').delete()
session.commit()
session.close()