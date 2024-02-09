# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []

for numero in range(1, 11):
    lista.append(numero)

print(lista)

lista_dobrada = [numero * 2 for numero in range(1, 11)]

print(lista_dobrada)