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
    "year":"chaves repetidas retornam o ultimo valor",
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

# mesmo lugar em memória
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = dict1
dict2['key1'] = 'other value'

# copia (swallow copy)
dict3 = dict1.copy()
dict3['key1'] = 'one more value'
print(dict1['key1'])


#------------ outro exemplo --------------

car_2 = copy.copy(car)
print(car, car_2)
car_2['owners'][0] = 'marinaldo'

print(car["owners"][0])

# no caso de deep copy usar o metodo copy.deepcopy, onde os subniveis do dicionário serão atingidos.

car_2_muito_poderoso_TURBO = copy.deepcopy(car)

print(car["owners"][0])
car_2_muito_poderoso_TURBO['owners'][0] = 'maria da feira'
print(car_2_muito_poderoso_TURBO['owners'][0])

# get() - obtem uma chave
ficougrande = car_2_muito_poderoso_TURBO.get(['owners'][0])

print(ficougrande)

#pop() - apaga um item com a chave especificada (del)

ultimos_donos = car_2_muito_poderoso_TURBO.pop(['owners'][0])

print(ultimos_donos)
print(car_2_muito_poderoso_TURBO)

# popitem() - apaga o último item adicionado
car_2_muito_poderoso_TURBO.popitem() #f kms
print(car_2_muito_poderoso_TURBO)

#update() - Atualiza um dicionário com outro

car_2_muito_poderoso_TURBO.update(car)
print(car_2_muito_poderoso_TURBO)

