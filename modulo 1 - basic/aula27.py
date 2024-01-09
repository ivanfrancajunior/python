# split strings e função len

# [inicio -> indice inicial : fatiamento - quantidade de caracteres : passo - intervalo entre o fatiamento ( 1 em 1 default)]

minha_string = 'minha string'

minha = minha_string[0:5]
string = minha_string[6:]

print(minha)
print(string)


# funçao len -> retorna a quantidade de caracteres de uma string

print(len(minha))
print(len(string))

'''
    Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:

Exiba:

    Seu nome é {nome}
    
    Seu nome invertido é {nome invertido}
    
    Seu nome contém (ou não) espaços
    
    Seu nome tem {n} letras
    
    A primeira letra do seu nome é {letra}
    
    A última letra do seu nome é {letra}
    
    Se nada for digitado em nome ou idade:
    
    exiba "Desculpe, você deixou campos vazios. "
'''

nome = input("Informe seu nome \n")

idade = input("Informe sua idade \n")

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.\n')

else:

    print(f'Seu nome é {nome}\n')

    print(f'Seu nome invertido é {nome[::-1]}\n')

    print(f"Seu nome possui {len(nome)} letras\n")

    if ' ' in nome: 
        print(f'Seu nome possui espaços.\n')
    else:
        print(f'Seu nome não possui espaços.\n')

    print(f"Seu nome inicia com {nome[0]}\n")

    print(f"Seu nome termina com {nome[-1]}\n")


