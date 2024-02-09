# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
# em https://youtu.be/1YbTDczvqco

'''List comprehension por baixo dos panos 

    lista = []

    for numero in range(1, 11):
        lista.append(numero)

    print(lista)
'''

#List comprehension
lista_dobrada = [numero * 2 for numero in range(1, 31)]
print(lista_dobrada)


# map e filter com list comprehension

# map
valores_maiores_que_cinco = [numero for numero in range(1, 31) if numero % 5 == 0]

print(valores_maiores_que_cinco)

# filter
valores_multiplos_de_tres = [numero for numero in range(1, 31) if numero % 3 == 0 ]

print(valores_multiplos_de_tres)
#------- outro exemplo --------

produtos = [ {'nome': 'p1', 'preco': 50}, {'nome': 'p2', 'preco': 30} ]


novos_produtos = [ {**produto,'nome': produto['nome'] + ' promocao', 'preco': round(produto['preco'] * 0.90)} for produto in produtos ]

print(novos_produtos)

array_dicts = [
    {'chave1': 'valor1', 'chave2': 'valor2'},
    {'chave1': 'valor3', 'chave2': 'valor4'},
    {'chave1': 'valor5', 'chave2': 'valor6'},
    {'chave1': 'valor7', 'chave2': 'valor8'},
    {'chave1': 'valor9', 'chave2': 'valor10'}
]

nv_array = [{**item,'chave1':item['chave1'] + ' alterado', 'chave2': item['chave2'] + ' alterado'} if len(array_dicts) > 4 else item for item in array_dicts] 
print(f"\n, {nv_array}")



