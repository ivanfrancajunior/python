# isinstance - checagem de tipos

lista = ['a',123,456,7,8,9,{'lala' : "lalala"}, 'sou uma string']

for item in lista:
    
    if isinstance(item,str):
        print(item.capitalize() + ' é') 

    print(isinstance(item,set), item)



