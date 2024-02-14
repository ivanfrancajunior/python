"""
Decoratoes

Decorators em Python são funções que permitem adicionar funcionalidades extras a outras funções ou métodos.

Eles são implementados usando a sintaxe @nome_do_decorator acima da definição da função que será decorada

"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada")
        result = func(*args, **kwargs)
        print("Depois da função ser chamada")
        return result
    return wrapper


@decorator
def minha_fn():
    print('Esta é minha funcao!')

minha_fn()

@decorator
def soma (a,b):
    return a + b

print('\n',soma(1,2))

def print_arg(func):
    
    def inside(*args, **kwargs):
        print(*args,**kwargs)
        result = func(*args, **kwargs)
    
        return result
    return inside

@print_arg
def fala_oi(nome):
    print(f'Oi, {nome}')

name= 'Mauro'
fala_oi(name)

def cria_linha(func):
    def inside(*args,**kwargs):
        print('------------------')
        result = func(*args,**kwargs)
        return result
    return inside

andre = 'Andre'

@cria_linha
def fala_ola(name):
    print(f'Olá, {name}')

fala_ola("Andre")


@cria_linha
def multiply(a,b):
    return a * b

resultado = multiply(1,1)

print(resultado)

def cria_duas_linhas(func):
    def inside(*args,**kwargs):
        print('=========================')
        res = func(*args,**kwargs)
        return res
    return inside

@cria_duas_linhas
def subtrair(a,b):
    return a - b

print(subtrair(1,1))