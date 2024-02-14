''' Recursividade:
    
    É um conceito onde uma função pode chamar a si mesma diretamente ou indiretamente para resolver um problema.

    # Toda função recursiva deve ter:
    # - Um problema que possa ser dividido em partes menores

    # - Um caso recursivo que resolve o pequeno problema

    # - Um caso base que para a recursão

    # - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

    # https://brasilescola.uol.com.br/matematica/fatorial.htm
'''

def fatorial(value):
    if value <= 1:
        return 1
    return value * fatorial(value -1)
   


print(fatorial(5))
# stack overflow: corre quando uma função recursiva chama a si mesma repetidamente sem alcançar o caso base, resultando em uma pilha de chamadas de função cada vez maior.

# def stack_overflow(inicio=0, fim=10):
#     inicio += 1
#     return  stack_overflow (inicio,fim)

# print(stack_overflow())

'''limite de recurções

    O limite de recursão em Python é o número máximo de chamadas de função que podem ser empilhadas na pilha de chamadas do sistema operacional. Quando esse limite é ultrapassado, ocorre um estouro de pilha (stack overflow). 
    
    O limite varia dependendo do sistema operacional e da configuração do interpretador Python, mas em geral é cerca de 1000 chamadas recursivas.

''' 

print(fatorial(999))
# print(fatorial(1000)) ❌