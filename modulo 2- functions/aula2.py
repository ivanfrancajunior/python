# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(* args):
    acc = 1
    
    for values in args:
        acc *= values
    return acc

six = multiply(1,2,3)

print(six)

# Crie uma função fala se um número é par ou ímpar

def isEven (value):
    
    if value % 2 == 0: 
        return (f'The number {value} is even.')
    
    return (f'The number {value} is odd.')

print(isEven(2))
print(isEven(3))
