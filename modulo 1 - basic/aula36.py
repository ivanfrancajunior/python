"""
LISTAS EM PYTHON

Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:

    append, 

    insert, 

    pop, 

    del, 

    clear,

    extend, 

    copy()




"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

lista.insert(0,75)
print(lista)

lista_a = [1, 2, 3]

lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

lista_a.extend(lista_b)

lista_b.extend(lista_a); 

print(lista_b)

print(lista_a)