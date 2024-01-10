# built-in types - https://docs.python.org/pt-br/3/library/stdtypes.html

""" LOOPS:

Repetições

while (enquanto)

Executa uma ação enquanto uma condição for verdadeira

Loop infinito -> Quando um código não tem fim

atribuições com '++' n existe em python :( 


"""

# count = 0 

# while count < 100:
#     print(count)

#     count += 1    

#     if count % 4 == 0 and count < 100:

#         print('plin!')
#     continue

# print('end')

# name = 'apenas jota'

# name_size = len(name)

# index = 0
# new_name = ''
# while index < name_size:
#     print(name[index])
#     new_name += f'*{name[index]}'
#     index += 1

# print(new_name)

# exercice - calculator 

while True:
    
    first = input('Type a value \n')
    if first.isdigit():
        value_one = float(first)
    else:
        print('Type a valid value')
        continue
    second = input('Type other value \n')
    
    if second.isdigit():
        second_value = float(second)
    else:
        print('Type a valid value')
        continue

    operation = input('Type a simbol of tour operation [ + | - | * | / ] \n')

    if len(operation) > 1:
        print('Please type only one operation.')
    else:
        if operation == "+" :
            
            result = value_one + second_value
            
            print(f'The result of your operation is {result}') 
        
            sair = input(" Type [S] to exit or press other key to continue." )
            if sair.lower().startswith('s'):
                break
            else: 
                continue
        
        elif operation == "-" :
            
            result = value_one - second_value
            
            print(f'The result of your operation is {result}') 

            sair = input(" Type [S] to exit or press other key to continue." )
            if sair.lower().startswith('s'):
                break
            else: 
                continue
        
        elif operation == "*" :
            
            result = value_one * second_value
            
            print(f'The result of your operation is {result}') 

            sair = input(" Type [S] to exit or press other key to continue." )
            if sair.lower().startswith('s'):
                break
            else: 
                continue
        
        else :
            
            result = value_one / second_value
            
            print(f'The result of your operation is {result}') 

            sair = input(" Type [S] to exit or press other key to continue." )
            if sair.lower().startswith('s'):
                break
            else: 
                continue
