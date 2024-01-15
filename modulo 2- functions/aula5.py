''' Métodos úteis dos dicionários em Python
    
    # len - quantas chaves
    # keys - iterável com as chaves
    # values - iterável com os valores
    # items - iterável com chaves e valores
    # setdefault - adiciona valor se a chave não existe
    # copy - retorna uma cópia rasa (shallow copy)
    # get - obtém uma chave
    # pop - Apaga um item com a chave especificada (del)
    # popitem - Apaga o último item adicionado
    # update - Atualiza um dicionário com outro

    '''
import copy

car = {
    "name":'Uninho de Firma',
    "label":"Fiat",
    "year":"96",
    "color":"red",
    "kms":"170",
    'owners':['serjin do açogue', 'roberto da padaria' ]
}

print(car.__len__()) # == len(car)
print(car.keys())
print(car.values())

car_tuple = car.items()
print(car_tuple, type(car_tuple))

# ATENÇÃO COM SHALOW COPY: dados mutaveis (listas e dicts ) usando 'copy' ainda mantêm a mesma ref. de memória.




car_2 = copy.copy(car)
print(car, car_2)
car_2['owners'][0] = 'marinaldo'

print(car["owners"][0])

# no caso de deep copy usar o metodo copy.deepcopy, onde os subniveis do dicionário serão atingidos.

car_2_turbo = copy.deepcopy(car)

print(car["owners"][0])
car_2_turbo['owners'][0] = 'maria da feira'
print(car_2_turbo['owners'][0])

