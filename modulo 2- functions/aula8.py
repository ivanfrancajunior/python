"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista = [1,2,3,4,4,5,6,7,8,8,9,5,1,]

def find_duplicates(arr):
    first_duplicate = -1
    checked_values = set()

    for value in arr:
        if value in checked_values:
            first_duplicate = value
            break
        checked_values.add(value)

    return first_duplicate

print(find_duplicates(lista))