# funçoes: 


def showName(name='user'):
    return print(name)

showName('Aderbal')



# valores padrao com argumentos nomeados
def somar (a, b, c=None):
    if c is not None:
        print (f"{a=} {b=} {c=}", a + b + c )
    else:
        print (f"{a=}  {b=}", a + b  )

somar(1,1,1)

# retorno de funçoes
def mostrarStringGerada ( ):

    def string():
        return print('Sou a string do closure')
    
    return string()

mostrarStringGerada()

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 'valor global de x'

# escopo de função
def escopo():
    global x # n  fazer isso ok, má pratica porém existe
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()


"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""


# args - Argumentos não nomeados
x, y, *rest = 1, 2, 3, 4
print(x, y, rest)


def soma(x, y):
    return x + y

def soma(*args):
    acc_total = 0
    for numero in args:
        acc_total += numero
    return acc_total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)


# sum() built-in function
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(type(numeros))

print(sum(numeros))