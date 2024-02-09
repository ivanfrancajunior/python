# HIGH ORDER FUNCTIONS

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Bensomn')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)

"""
Closure e funções que retornam outras funções

** Um "closure" em programação ocorre quando uma função interna (função aninhada) tem acesso às variáveis locais de uma função externa, mesmo após a função externa ter concluído sua execução. Isso significa que a função interna "lembra" do ambiente em que foi criada.

"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(bom_dia(nome))
    print(boa_noite(nome))


'''
Exercicio:
crie uma função que duplica, triplica e quadruplica um número 
''' 
def multiply_by(value):
    
    def multiply(base):
        return base * value
    return multiply

dobble = multiply_by(2)
triple = multiply_by(3)
quadruple = multiply_by(4)
print(dobble(10))
print(triple(10))
print(quadruple(10))