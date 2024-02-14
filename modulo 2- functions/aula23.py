"""zip funtion 

A função zip em Python é utilizada para combinar elementos de duas ou mais sequências (como listas, tuplas, etc.) em pares ordenados. 

Ela cria um iterador que gera tuplas, onde o i-ésimo elemento de cada sequência é agrupado juntamente. Se as sequências tiverem tamanhos diferentes, o iterador produzirá tuplas até que a menor sequência se esgote. 

"""
# def soma_arrays(lista_1,lista_2):
#     tamanho = 0
#     nova_lista = []
   
#     if len(lista_1) > len(lista_2):
#         tamanho = len(lista_2)
#     else:
#         tamanho = len(lista_1)
    
#     for i in range(tamanho):
#         nova_lista.append(lista_1[i] + lista_2[i])
    
#     return nova_lista

# result = soma_arrays([1,2,3,4],[1,2,3,4,5,6])
# print(result)

lista_1 = [1,2,3,4]
lista_2 = [1,2,3,4,5,6]

result = [x + y  for x,y in zip(lista_1,lista_2) ]
print(result)