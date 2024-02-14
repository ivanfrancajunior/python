fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# list_fruits = []
# for fruit in fruits:
#     if 'a' in fruit:
#         list_fruits.append(fruit)
# print(list_fruits)


list_fruits = [fruit for fruit in fruits if 'e' in fruit]

print(list_fruits)

numbers = [3,6,9,12,15,18,21,24,27,30]

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers) # expect only odd numbers

multyple_of_four = [number for number in range(1,513) if number % 4 == 0 and number % 3 == 0]

print(multyple_of_four)

list = [1,2,3,4]

nova_lista = [*list]
print('\n',nova_lista)

lista_de_dicionarios = [
    {'nome': 'Item1', 'valor': 10},
    {'nome': 'Item2', 'valor': 20},
    {'nome': 'Item3', 'valor': 30},
    {'nome': 'Item4', 'valor': 40},
    {'nome': 'Item5', 'valor': 50}
]

list_with_att_values =[{'nome': item['nome'], 'price':round(item['valor']*1.1,2) } for item in lista_de_dicionarios]

print(list_with_att_values)