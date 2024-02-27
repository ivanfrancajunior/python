'''

Exercícios sobre o uso do SQLAlchemy:

1. **Criar uma base de dados:**
   - Crie um novo banco de dados SQLite usando SQLAlchemy.
   - Defina uma tabela chamada "Usuários" com os campos: ID (chave primária), Nome e Idade.

2. **Inserir dados:**
   - Insira alguns registros na tabela "Usuários" usando objetos Python.

3. **Consultar dados:**
   - Execute consultas para recuperar todos os registros da tabela "Usuários".
   - Execute consultas para recuperar usuários com idade superior a 30 anos.

4. **Atualizar dados:**
   - Atualize a idade de um usuário específico na tabela "Usuários".

5. **Excluir dados:**
   - Exclua um usuário específico da tabela "Usuários" com base no ID.

6. **Relacionamentos entre tabelas:**
   - Crie uma nova tabela chamada "Pedidos" com os campos: ID (chave primária), ID do usuário (chave estrangeira), Nome do produto e Quantidade.
   - Defina um relacionamento entre a tabela "Usuários" e a tabela "Pedidos".

7. **Consultas avançadas:**
   - Execute uma consulta para recuperar todos os usuários juntamente com seus respectivos pedidos.
   - Execute uma consulta para recuperar todos os usuários que fizeram pedidos de um produto específico.

8. **Alterações no esquema:**
   - Adicione um novo campo à tabela "Usuários", como "Email" ou "Endereço".
   - Remova o campo "Idade" da tabela "Usuários".

9. **Transações:**
   - Execute operações de inserção, atualização e exclusão dentro de uma transação.
   - Realize o commit da transação para salvar as alterações no banco de dados.
   - Realize um rollback para desfazer as alterações feitas em uma transação.

10. **Gerenciamento de sessão:**
   - Crie uma sessão do SQLAlchemy para interagir com o banco de dados.
   - Use a sessão para executar consultas, inserções, atualizações e exclusões de registros.

Esses exercícios fornecem uma variedade de tarefas para praticar diferentes aspectos do SQLAlchemy, desde a criação básica de bancos de dados e tabelas até consultas avançadas e alterações no esquema.


'''
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from uuid import uuid4
sqlite_engine = create_engine("sqlite:///exec_v1.db")
connect= sqlite_engine.connect()

if connect:  
    print('running')

class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__='usuarios'
    id = Column(String,primary_key=True)
    nome = Column(String,nullable=False)
    idade = Column(Integer,nullable=False)

    def __repr__(self) -> str:
        return f'Usuário(titulo={self.id}, genero={self.nome}, ano={self.idade}'
    

#cria a base altomaticamente a partir da classe
Usuario.metadata.create_all(sqlite_engine)
Session = sessionmaker(bind=sqlite_engine)

session = Session()
novo_usuario:Usuario = Usuario(id=str(uuid4()),nome='Marcelo Martelo',idade=30 )

nova_usuaria:Usuario = Usuario(id=str(uuid4()),nome='Erisa Beta',idade=25 )

novo_usuario2:Usuario = Usuario(id=str(uuid4()),nome='Marisvaldo Gosta de Placices ',idade=35 )

nova_usuaria2:Usuario = Usuario(id=str(uuid4()),nome='Maria Monte ',idade=36 )

session.add(nova_usuaria)
session.commit()
session.close()

session.add( novo_usuario2)
session.commit()
session.close()

session.add(nova_usuaria2)
session.commit()
session.close()

data = session.query(Usuario).all()
print(data)

tirdy_plus = session.query(Usuario).filter(Usuario.idade >= '30').all()

print('/n','here -> ',tirdy_plus)

marisa_monte = session.query(Usuario).filter(Usuario.id == '705606b5-dc53-487b-bb36-e9c84146f85f').update({'nome':'Marisa Monte'})

session.commit()
session.close()
