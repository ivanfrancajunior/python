'''
    # Generator expression, Iterables e Iterators em Python
   
    # armazena apenas um valor na memoria até a prox execução 
    # não da acesso ao indices dos valores
    # não da acesso ao tamanho da lista
    # é possivel usar o next assim como os iterators
'''

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

print(next(generator) )
print(next(generator) )
print(next(generator) )

# for n in generator:
#     print(n)
'''
    # Introdução às Generator functions em Python
    
    # generator = (n for n in range(1000000))

    yield é uma palavra-chave usada em funções geradoras para criar iteradores de forma eficiente. Quando uma função contém a palavra-chave yield, ela se torna um generator.     
    '''

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)

# yield from 
    