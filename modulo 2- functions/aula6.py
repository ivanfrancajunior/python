# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count = 0
print('Responda as perguntas com o valor correspondente: \n')

print(perguntas[0]['Pergunta'])

for opc in perguntas[0]['Opções']:
    print(opc)
resp1 = input("Digite sua resposta: \n")

if resp1 in perguntas[0]["Opções"] and resp1 == perguntas[0]["Resposta"]:

    print('Voce acertou !!!!')
    count += 1
else:
    print(f'A resposta correta é {perguntas[0]["Resposta"]}')

if resp1 not in perguntas[0]['Opções']:

    print("Digite apenas as opções válidas.")
    print(f'A resposta correta é {perguntas[0]["Resposta"]}')


print("\n")

print(perguntas[1]['Pergunta'])

for opc in perguntas[1]['Opções']:
    print(opc)
resp1 = input("Digite sua resposta: \n")

if resp1 in perguntas[1]["Opções"] and resp1 == perguntas[1]["Resposta"]:

    print('Voce acertou !!!!')
    count += 1
else:
    print(f'A resposta correta é {perguntas[1]["Resposta"]}')

print("\n")
print(perguntas[2]['Pergunta'])

for opc in perguntas[2]['Opções']:
    print(opc)
resp1 = input("Digite sua resposta: \n")

if resp1 in perguntas[2]["Opções"] and resp1 == perguntas[2]["Resposta"]:

    print('Voce acertou !!!!')
    count += 1
else:
    print(f'A resposta correta é {perguntas[2]["Resposta"]}')

print(f'Fim do jogo, voce acertou {count} de {len(perguntas)} perguntas')

'''
    resposta: 
    # Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

'''