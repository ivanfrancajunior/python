# Loops - for in 

# palavra = 'Python'
# count = 1
# for letra in palavra:
#     print(letra , ' - ', count)
#     count += 1 


# '''
#     range
#    range(star, stop, step)
# ''' 

# numeros = range(0,10)
# print(numeros)

# for numero  in numeros:
#     print(numero)

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Jota'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)