
# # Operadores condicionais


# entrada = input('Você quer "sair" ou "entrar?"\n ')

# if entrada == "entrar":
#     print("Bem vindo de volta") 
# elif entrada == 'sair':
#     print('Até breve!')
# else:
#     print('Opção não encontrada :(')


# exercicio:
    
# primeiro_valor = input('Digite um numero \n')

# segundo_valor = input('Digite um numero \n')

# if primeiro_valor > segundo_valor:
#     print(f'O primeiro {primeiro_valor} valor é maior que o segundo {segundo_valor}! ')
# elif primeiro_valor == segundo_valor:
#     print(f'Os valores {primeiro_valor} e {segundo_valor} são iguais!')
# else:
#     print(f'O Segundo {segundo_valor} valor é maior que o primeiro {primeiro_valor}!')

"""
    Operadores lógicos: 

and -> 'e' ==               &  
or -> "ou"                  ||
not -> "not"                !=

-------------------------------------------------------
Operadores IN e NOT IN

in -> entre                 
not in -> não esta entre         

"""

# operacao = input('[E]entrar [S]air \n')

# senha = input("Digite sua senha \n")

# if not senha: 
#     print('Operação inválida')

# elif (operacao == "E" or operacao == 'e') and senha == '123456':
#     print('Acesso permitido') 

# elif (operacao == "S" or operacao == 's') and senha == '123456':
#     print('Saiu') 

# else:
#     print('Senha inválida!')


print(29 * '-')

nome_teste = 'Travis Scott'

if 'Travis' in nome_teste : 
    print("É o Trev não há maneiras 😎 ")
elif "Travis" not in nome_teste:
    print('Claramente não é o Trev...')

"""
Interpolação de strings

s - strings
d e i - int
f - float
x e X - hexadecimal

"""
print(29 * '-')
    
nome_arthur = 'Arthur'
idade_arthur = 7

string_arthur = 'Este é o %s , ele tem %i anos. '% (nome_arthur, idade_arthur)

print(string_arthur)
