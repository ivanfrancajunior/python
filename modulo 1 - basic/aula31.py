"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# user_number = input('Type a number: \n')

# try :
#     if not user_number or not user_number.isdigit():
#         print('Type a valid value.')

#     int_number = float(user_number)

#     isEven = int_number % 2 == 0
        
#     if isEven: 
#        print(f'The number {int_number:.0f} is a even value.')
#     else:
#        print(f'The number {int_number:.0f} isn\'t  a even value.')

# except:
#  print('try again')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# user_hour = input('Type a hour: ')

# if user_hour.isdigit():
#     valid_hour = int(user_hour)

#     if valid_hour > 0 and valid_hour <= 11:
#         print('Good morning sunshine :)')   
#     elif valid_hour > 11 and valid_hour <= 17:
#         print('Good aftermoon my friend') 
#     else:  
#         print('Good nigth boddy')
# else: 
#     print('Please type a valid value.')    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

user_name = input('Digit your name: \n')

if user_name and not user_name.isdigit():
    name_size = len(user_name)
    if name_size <= 4:
        print('You have a short name.')
    elif name_size >4 and name_size <= 6:
        print('You have a regular name size')
    else:
        print('Your name is big.')
else:
    print('Invalid value, try again.')